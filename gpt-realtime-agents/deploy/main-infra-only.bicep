// Infrastructure only: ACR + Container Apps Environment (no Container App)
targetScope = 'resourceGroup'

@description('Base name for resources')
param baseName string = 'contoso'

@description('Location for all resources')
param location string = resourceGroup().location

// Generate unique suffix
var uniqueSuffix = uniqueString(resourceGroup().id)
var acrName = '${baseName}${uniqueSuffix}'
var containerAppEnvName = '${baseName}-env-${uniqueSuffix}'
var logAnalyticsName = '${baseName}-logs-${uniqueSuffix}'

var tags = {
  application: 'Contoso AI Commerce'
  environment: 'production'
}

// 1. Log Analytics Workspace
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
    adminUserEnabled: true
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

// Outputs
output acrLoginServer string = acr.properties.loginServer
output acrName string = acr.name
output acrUsername string = acr.listCredentials().username
output acrPassword string = acr.listCredentials().passwords[0].value
output containerEnvName string = containerAppEnv.name
output containerEnvId string = containerAppEnv.id
output resourceGroupName string = resourceGroup().name
output location string = location
