#!/usr/bin/env pwsh
# Single deployment script: Infrastructure + Build + Deploy
# Handles multiple apps in the same resource group without conflicts

param(
    [Parameter(Mandatory=$false)]
    [string]$ResourceGroupName = "rg-contosoaicommerce",

    [Parameter(Mandatory=$false)]
    [string]$Location = "eastus2",

    [Parameter(Mandatory=$false)]
    [string]$ImageTag = "latest",

    [Parameter(Mandatory=$false)]
    [string]$SubscriptionId = "b4b0289a-cba8-45f6-ad48-a9d21908f648",

    [Parameter(Mandatory=$false)]
    [string]$AppName = "contoso-bet",  # Unique app name (e.g., contoso-bet, contoso-commerce, contoso-vodafone)

    [Parameter(Mandatory=$false)]
    [string]$BaseName = "contoso"  # Base name for shared infrastructure (ACR, Environment)
)

$ErrorActionPreference = "Stop"

Write-Host ""
Write-Host "=========================================================" -ForegroundColor Cyan
Write-Host "   Deploying: $AppName" -ForegroundColor Cyan
Write-Host "   Resource Group: $ResourceGroupName" -ForegroundColor Cyan
Write-Host "   Location: $Location" -ForegroundColor Cyan
Write-Host "=========================================================" -ForegroundColor Cyan
Write-Host ""

# ============================================================================
# STEP 1: Azure Login & Subscription
# ============================================================================
Write-Host "[1/5] Checking Azure login..." -ForegroundColor Yellow
$account = az account show 2>$null | ConvertFrom-Json
if (-not $account) {
    Write-Host "Not logged in to Azure. Please run 'az login --tenant fdpo.onmicrosoft.com' first." -ForegroundColor Red
    exit 1
}
Write-Host "Logged in as: $($account.user.name)" -ForegroundColor Green

Write-Host "Setting subscription: $SubscriptionId..." -ForegroundColor Yellow
az account set --subscription $SubscriptionId
if ($LASTEXITCODE -ne 0) {
    Write-Host "Failed to set subscription. Run: az login --tenant fdpo.onmicrosoft.com" -ForegroundColor Red
    exit 1
}
$account = az account show | ConvertFrom-Json
Write-Host "Subscription: $($account.name)" -ForegroundColor Green
Write-Host ""

# ============================================================================
# STEP 2: Create/Verify Resource Group
# ============================================================================
Write-Host "[2/5] Creating resource group..." -ForegroundColor Yellow
az group create --name $ResourceGroupName --location $Location --output none
if ($LASTEXITCODE -ne 0) {
    Write-Host "Failed to create resource group" -ForegroundColor Red
    exit 1
}
Write-Host "Resource group ready: $ResourceGroupName" -ForegroundColor Green
Write-Host ""

# ============================================================================
# STEP 3: Deploy Infrastructure (ACR + Container Apps Environment)
# ============================================================================
Write-Host "[3/5] Deploying infrastructure (ACR + Environment)..." -ForegroundColor Yellow

Set-Location $PSScriptRoot
$infraDeploymentName = "$BaseName-infra-$(Get-Date -Format 'yyyyMMdd-HHmmss')"

$infraDeployment = az deployment group create `
    --name $infraDeploymentName `
    --resource-group $ResourceGroupName `
    --template-file main-infra-only.bicep `
    --parameters location=$Location baseName=$BaseName `
    --output json | ConvertFrom-Json

if ($LASTEXITCODE -ne 0) {
    Write-Host "Infrastructure deployment failed" -ForegroundColor Red
    exit 1
}

$infraOutputs = $infraDeployment.properties.outputs
$acrName = $infraOutputs.acrName.value
$acrLoginServer = $infraOutputs.acrLoginServer.value
$acrUsername = $infraOutputs.acrUsername.value
$acrPassword = $infraOutputs.acrPassword.value
$containerEnvId = $infraOutputs.containerEnvId.value

Write-Host "Infrastructure ready:" -ForegroundColor Green
Write-Host "  ACR: $acrLoginServer" -ForegroundColor Gray
Write-Host "  Environment: $($infraOutputs.containerEnvName.value)" -ForegroundColor Gray
Write-Host ""

# ============================================================================
# STEP 4: Build and Push Docker Image
# ============================================================================
Write-Host "[4/5] Building and pushing Docker image..." -ForegroundColor Yellow

$projectRoot = Split-Path $PSScriptRoot -Parent
Set-Location $projectRoot

# Login to ACR
az acr login --name $acrName
if ($LASTEXITCODE -ne 0) {
    Write-Host "Failed to login to ACR" -ForegroundColor Red
    exit 1
}

$fullImageName = "${acrLoginServer}/${AppName}:${ImageTag}"
Write-Host "Building: $fullImageName" -ForegroundColor Gray

# Force rebuild to pick up frontend changes
docker build --no-cache -t $fullImageName -f Dockerfile .
if ($LASTEXITCODE -ne 0) {
    Write-Host "Docker build failed" -ForegroundColor Red
    exit 1
}

docker push $fullImageName
if ($LASTEXITCODE -ne 0) {
    Write-Host "Docker push failed" -ForegroundColor Red
    exit 1
}
Write-Host "Image pushed: $fullImageName" -ForegroundColor Green
Write-Host ""

# ============================================================================
# STEP 5: Deploy Container App
# ============================================================================
Write-Host "[5/5] Deploying Container App: $AppName..." -ForegroundColor Yellow

# Read .env file for Azure OpenAI configuration
$envFile = Join-Path $projectRoot ".env"
$envVars = @{}
Get-Content $envFile | ForEach-Object {
    if ($_ -match '^\s*([^#][^=]+)=(.+)$') {
        $key = $matches[1].Trim()
        $value = $matches[2].Trim().Trim('"')
        $envVars[$key] = $value
    }
}

if (-not $envVars['AZURE_GPT_REALTIME_URL']) {
    Write-Host "Missing AZURE_GPT_REALTIME_URL in .env file" -ForegroundColor Red
    exit 1
}

Set-Location $PSScriptRoot
$appDeploymentName = "$AppName-$(Get-Date -Format 'yyyyMMdd-HHmmss')"

$appDeployment = az deployment group create `
    --name $appDeploymentName `
    --resource-group $ResourceGroupName `
    --template-file main-app-only.bicep `
    --parameters `
        "appName=$AppName" `
        "imageName=$AppName" `
        location=$Location `
        imageTag=$ImageTag `
        "acrLoginServer=$acrLoginServer" `
        "acrUsername=$acrUsername" `
        "acrPassword=$acrPassword" `
        "containerEnvId=$containerEnvId" `
        "azureGptRealtimeUrl=$($envVars['AZURE_GPT_REALTIME_URL'])" `
        "webrtcUrl=$($envVars['WEBRTC_URL'])" `
        "azureGptRealtimeDeployment=$($envVars['AZURE_GPT_REALTIME_DEPLOYMENT'])" `
        "azureGptRealtimeVoice=$($envVars['AZURE_GPT_REALTIME_VOICE'])" `
    --output json | ConvertFrom-Json

if ($LASTEXITCODE -ne 0) {
    Write-Host "Container App deployment failed" -ForegroundColor Red
    exit 1
}

$appOutputs = $appDeployment.properties.outputs

# ============================================================================
# DONE - Show Results
# ============================================================================
Write-Host ""
Write-Host "=========================================================" -ForegroundColor Green
Write-Host "   DEPLOYMENT SUCCESSFUL" -ForegroundColor Green
Write-Host "=========================================================" -ForegroundColor Green
Write-Host ""
Write-Host "App URL:      $($appOutputs.containerAppUrl.value)" -ForegroundColor White
Write-Host "App Name:     $($appOutputs.containerAppName.value)" -ForegroundColor Gray
Write-Host "Principal ID: $($appOutputs.containerAppPrincipalId.value)" -ForegroundColor Gray
Write-Host ""
Write-Host "IMPORTANT: Assign Cognitive Services User role:" -ForegroundColor Yellow
Write-Host ""
Write-Host "az role assignment create --assignee $($appOutputs.containerAppPrincipalId.value) --role 'Cognitive Services User' --scope /subscriptions/$SubscriptionId/resourceGroups/<openai-rg>/providers/Microsoft.CognitiveServices/accounts/<openai-account>" -ForegroundColor Cyan
Write-Host ""
Write-Host "View logs:" -ForegroundColor Gray
Write-Host "az containerapp logs show --name $($appOutputs.containerAppName.value) --resource-group $ResourceGroupName --follow" -ForegroundColor Gray
Write-Host ""

# Save outputs
$allOutputs = @{
    appName = $AppName
    appUrl = $appOutputs.containerAppUrl.value
    containerAppName = $appOutputs.containerAppName.value
    principalId = $appOutputs.containerAppPrincipalId.value
    acrLoginServer = $acrLoginServer
    resourceGroup = $ResourceGroupName
}
$outputsFile = Join-Path $PSScriptRoot "deployment-$AppName.json"
$allOutputs | ConvertTo-Json -Depth 10 | Set-Content $outputsFile
Write-Host "Outputs saved to: deployment-$AppName.json" -ForegroundColor Gray
Write-Host ""
