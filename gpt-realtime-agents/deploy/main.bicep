// Simplified Azure Container Apps deployment for Contoso AI Commerce
targetScope = 'resourceGroup'

@description('Base name for resources (will be suffixed with unique string)')
param baseName string = 'travelagent'

@description('Location for all resources')
param location string = resourceGroup().location

@description('Docker image tag to deploy')
param imageTag string = 'latest'

@description('Azure OpenAI Realtime URL')
param azureGptRealtimeUrl string

@description('WebRTC URL')
param webrtcUrl string

@description('Azure OpenAI Realtime API Key')
@secure()
param azureGptRealtimeKey string

@description('Azure OpenAI Realtime Deployment Name')
param azureGptRealtimeDeployment string = 'gpt-realtime-2'

@description('Azure OpenAI Realtime Voice')
param azureGptRealtimeVoice string = 'verse'

// Generate unique suffix for globally unique resources
var uniqueSuffix = uniqueString(resourceGroup().id)
var acrName = '${baseName}${uniqueSuffix}' // ACR name must be alphanumeric only
var containerAppEnvName = '${baseName}-env-${uniqueSuffix}'
var containerAppName = '${baseName}-app-${uniqueSuffix}'
var logAnalyticsName = '${baseName}-logs-${uniqueSuffix}'

// Tags for all resources
var tags = {
  application: 'Travel Agent'
  environment: 'production'
}

// 1. Log Analytics Workspace (required for Container Apps Environment)
resource logAnalytics 'Microsoft.OperationalInsights/workspaces@2022-10-01' = {
  name: logAnalyticsName
  location: location
  tags: tags
  properties: {
    sku: {
      name: 'PerGB2018'
    }
    retentionInDays: 30
  }
}

// 2. Azure Container Registry
resource acr 'Microsoft.ContainerRegistry/registries@2023-01-01-preview' = {
  name: acrName
  location: location
  tags: tags
  sku: {
    name: 'Basic'
  }
  properties: {
    adminUserEnabled: true // Enable admin user for easy docker login
  }
}

// 3. Container Apps Environment
resource containerAppEnv 'Microsoft.App/managedEnvironments@2023-05-01' = {
  name: containerAppEnvName
  location: location
  tags: tags
  properties: {
    appLogsConfiguration: {
      destination: 'log-analytics'
      logAnalyticsConfiguration: {
        customerId: logAnalytics.properties.customerId
        sharedKey: logAnalytics.listKeys().primarySharedKey
      }
    }
  }
}

// 4. Container App
resource containerApp 'Microsoft.App/containerApps@2023-05-01' = {
  name: containerAppName
  location: location
  tags: tags
  properties: {
    managedEnvironmentId: containerAppEnv.id
    configuration: {
      ingress: {
        external: true
        targetPort: 8080
        allowInsecure: false
        traffic: [
          {
            latestRevision: true
            weight: 100
          }
        ]
      }
      registries: [
        {
          server: acr.properties.loginServer
          username: acr.listCredentials().username
          passwordSecretRef: 'acr-password'
        }
      ]
      secrets: [
        {
          name: 'acr-password'
          value: acr.listCredentials().passwords[0].value
        }
        {
          name: 'azure-gpt-realtime-key'
          value: azureGptRealtimeKey
        }
      ]
    }
    template: {
      containers: [
        {
          name: 'travelagent'
          image: '${acr.properties.loginServer}/${baseName}:${imageTag}'
          resources: {
            cpu: json('1.0')
            memory: '2Gi'
          }
          env: [
            {
              name: 'AZURE_GPT_REALTIME_URL'
              value: azureGptRealtimeUrl
            }
            {
              name: 'WEBRTC_URL'
              value: webrtcUrl
            }
            {
              name: 'AZURE_GPT_REALTIME_KEY'
              secretRef: 'azure-gpt-realtime-key'
            }
            {
              name: 'AZURE_GPT_REALTIME_DEPLOYMENT'
              value: azureGptRealtimeDeployment
            }
            {
              name: 'AZURE_GPT_REALTIME_VOICE'
              value: azureGptRealtimeVoice
            }
            {
              name: 'VITE_BACKEND_BASE_URL'
              value: 'https://${containerAppName}.${containerAppEnv.properties.defaultDomain}/api'
            }
          ]
        }
      ]
      scale: {
        minReplicas: 1
        maxReplicas: 3
      }
    }
  }
}

// Outputs
output acrLoginServer string = acr.properties.loginServer
output acrName string = acr.name
output acrUsername string = acr.listCredentials().username
output containerAppUrl string = 'https://${containerApp.properties.configuration.ingress.fqdn}'
output containerAppName string = containerApp.name
output resourceGroupName string = resourceGroup().name
