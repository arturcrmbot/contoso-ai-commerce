// Create Container App only (after image is pushed)
targetScope = 'resourceGroup'

@description('Unique app name for this deployment (e.g., contoso-bet, contoso-commerce)')
param appName string = 'contoso-bet'

@description('Image name in ACR (defaults to appName)')
param imageName string = ''

@description('Location for all resources')
param location string = resourceGroup().location

@description('Docker image tag to deploy')
param imageTag string = 'latest'

@description('ACR login server')
param acrLoginServer string

@description('ACR username')
param acrUsername string

@description('ACR password')
@secure()
param acrPassword string

@description('Container Apps Environment ID')
param containerEnvId string

@description('Azure OpenAI Realtime URL')
param azureGptRealtimeUrl string

@description('WebRTC URL')
param webrtcUrl string

@description('Azure OpenAI Resource ID for role assignment')
param azureOpenAIResourceId string = ''

@description('Azure OpenAI Realtime Deployment Name')
param azureGptRealtimeDeployment string = 'gpt-realtime-2'

@description('Azure OpenAI Realtime Voice')
param azureGptRealtimeVoice string = 'ballad'

// Use appName directly as container app name (caller provides unique name)
var containerAppName = appName
var actualImageName = empty(imageName) ? appName : imageName

var tags = {
  application: appName
  environment: 'production'
}

// Reference the existing Container Apps Environment to get its domain
resource containerAppEnv 'Microsoft.App/managedEnvironments@2023-05-01' existing = {
  name: split(containerEnvId, '/')[8]  // Extract name from resource ID
}

// Container App with system-assigned managed identity
resource containerApp 'Microsoft.App/containerApps@2023-05-01' = {
  name: containerAppName
  location: location
  tags: tags
  identity: {
    type: 'SystemAssigned'
  }
  properties: {
    managedEnvironmentId: containerEnvId
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
          server: acrLoginServer
          username: acrUsername
          passwordSecretRef: 'acr-password'
        }
      ]
      secrets: [
        {
          name: 'acr-password'
          value: acrPassword
        }
      ]
    }
    template: {
      containers: [
        {
          name: 'contoso-ai-commerce'
          image: '${acrLoginServer}/${actualImageName}:${imageTag}'
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

// Role assignment: Cognitive Services User role for the Container App's managed identity
// This allows the app to authenticate to Azure OpenAI using DefaultAzureCredential
resource cognitiveServicesUserRole 'Microsoft.Authorization/roleAssignments@2022-04-01' = if (!empty(azureOpenAIResourceId)) {
  name: guid(containerApp.id, azureOpenAIResourceId, 'cognitive-services-user')
  scope: resourceGroup()
  properties: {
    roleDefinitionId: subscriptionResourceId('Microsoft.Authorization/roleDefinitions', 'a97b65f3-24c7-4388-baec-2e87135dc908') // Cognitive Services User
    principalId: containerApp.identity.principalId
    principalType: 'ServicePrincipal'
  }
}

// Outputs
output containerAppName string = containerApp.name
output containerAppUrl string = 'https://${containerApp.properties.configuration.ingress.fqdn}'
output containerAppFqdn string = containerApp.properties.configuration.ingress.fqdn
output containerAppPrincipalId string = containerApp.identity.principalId
