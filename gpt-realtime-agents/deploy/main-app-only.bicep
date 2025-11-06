// Create Container App only (after image is pushed)
targetScope = 'resourceGroup'

@description('Base name for resources')
param baseName string = 'contoso'

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

@description('Azure OpenAI Realtime API Key')
@secure()
param azureGptRealtimeKey string

@description('Azure OpenAI Realtime Deployment Name')
param azureGptRealtimeDeployment string = 'gpt-realtime-2'

@description('Azure OpenAI Realtime Voice')
param azureGptRealtimeVoice string = 'verse'

var uniqueSuffix = uniqueString(resourceGroup().id)
var containerAppName = '${baseName}-app-${uniqueSuffix}'

var tags = {
  application: 'Contoso AI Commerce'
  environment: 'production'
}

// Container App
resource containerApp 'Microsoft.App/containerApps@2023-05-01' = {
  name: containerAppName
  location: location
  tags: tags
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
        {
          name: 'azure-gpt-realtime-key'
          value: azureGptRealtimeKey
        }
      ]
    }
    template: {
      containers: [
        {
          name: 'contoso-ai-commerce'
          image: '${acrLoginServer}/${baseName}:${imageTag}'
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
output containerAppName string = containerApp.name
output containerAppUrl string = 'https://${containerApp.properties.configuration.ingress.fqdn}'
output containerAppFqdn string = containerApp.properties.configuration.ingress.fqdn
