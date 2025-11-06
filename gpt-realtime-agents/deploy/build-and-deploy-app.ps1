#!/usr/bin/env pwsh
# Build Docker image, push to ACR, and create Container App

param(
    [Parameter(Mandatory=$false)]
    [string]$ImageTag = "latest",

    [Parameter(Mandatory=$false)]
    [string]$ResourceGroupName = "rg-contosoaicommerce"
)

$ErrorActionPreference = "Stop"

Write-Host "🐳 Contoso AI Commerce - Build & Deploy App" -ForegroundColor Cyan
Write-Host "===========================================" -ForegroundColor Cyan
Write-Host ""

# Check if infra outputs exist
$infraOutputsFile = Join-Path $PSScriptRoot "infra-outputs.json"
if (-not (Test-Path $infraOutputsFile)) {
    Write-Host "❌ Infrastructure outputs not found. Please run './deploy-infra-only.ps1' first." -ForegroundColor Red
    exit 1
}

$infraOutputs = Get-Content $infraOutputsFile | ConvertFrom-Json
$acrName = $infraOutputs.acrName.value
$acrLoginServer = $infraOutputs.acrLoginServer.value
$acrUsername = $infraOutputs.acrUsername.value
$acrPassword = $infraOutputs.acrPassword.value
$containerEnvId = $infraOutputs.containerEnvId.value
$location = $infraOutputs.location.value

Write-Host "📋 Using Infrastructure:" -ForegroundColor Yellow
Write-Host "   ACR: $acrLoginServer" -ForegroundColor Gray
Write-Host "   Resource Group: $ResourceGroupName" -ForegroundColor Gray
Write-Host ""

# Navigate to project root
$projectRoot = Split-Path $PSScriptRoot -Parent
Set-Location $projectRoot

# Login to ACR
Write-Host "🔐 Logging in to Azure Container Registry..." -ForegroundColor Yellow
az acr login --name $acrName
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Failed to login to ACR" -ForegroundColor Red
    exit 1
}
Write-Host "✅ Logged in to ACR" -ForegroundColor Green
Write-Host ""

# Build Docker image
$imageName = "contoso"
$fullImageName = "${acrLoginServer}/${imageName}:${ImageTag}"

Write-Host "🏗️  Building Docker image: $fullImageName" -ForegroundColor Yellow
Write-Host "   This may take 5-10 minutes..." -ForegroundColor Gray
docker build -t $fullImageName -f Dockerfile .
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Docker build failed" -ForegroundColor Red
    exit 1
}
Write-Host "✅ Docker image built successfully" -ForegroundColor Green
Write-Host ""

# Push to ACR
Write-Host "☁️  Pushing image to Azure Container Registry..." -ForegroundColor Yellow
docker push $fullImageName
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Docker push failed" -ForegroundColor Red
    exit 1
}
Write-Host "✅ Image pushed successfully" -ForegroundColor Green
Write-Host ""

# Read .env file for Azure OpenAI credentials
Write-Host "📄 Reading Azure OpenAI credentials from .env..." -ForegroundColor Yellow
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
    Write-Host "❌ Missing AZURE_GPT_REALTIME_URL in .env file" -ForegroundColor Red
    exit 1
}

Write-Host "✅ Credentials loaded" -ForegroundColor Green
Write-Host ""

# Deploy Container App
Write-Host "🚀 Creating Container App..." -ForegroundColor Yellow
$deploymentName = "contoso-app-$(Get-Date -Format 'yyyyMMdd-HHmmss')"

Set-Location $PSScriptRoot

$deployment = az deployment group create `
    --name $deploymentName `
    --resource-group $ResourceGroupName `
    --template-file main-app-only.bicep `
    --parameters `
        location=$location `
        imageTag=$ImageTag `
        acrLoginServer=$acrLoginServer `
        acrUsername=$acrUsername `
        acrPassword=$acrPassword `
        containerEnvId=$containerEnvId `
        azureGptRealtimeUrl=$envVars['AZURE_GPT_REALTIME_URL'] `
        webrtcUrl=$envVars['WEBRTC_URL'] `
        azureGptRealtimeKey=$envVars['AZURE_GPT_REALTIME_KEY'] `
        azureGptRealtimeDeployment=$envVars['AZURE_GPT_REALTIME_DEPLOYMENT'] `
        azureGptRealtimeVoice=$envVars['AZURE_GPT_REALTIME_VOICE'] `
    --output json | ConvertFrom-Json

if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Container App deployment failed" -ForegroundColor Red
    exit 1
}

Write-Host "✅ Container App deployed" -ForegroundColor Green
Write-Host ""

# Extract outputs
$outputs = $deployment.properties.outputs

Write-Host "🎉 Deployment Complete!" -ForegroundColor Green
Write-Host ""
Write-Host "📊 Your Application:" -ForegroundColor Cyan
Write-Host "=====================================" -ForegroundColor Cyan
Write-Host "App Name: $($outputs.containerAppName.value)" -ForegroundColor White
Write-Host "App URL:  $($outputs.containerAppUrl.value)" -ForegroundColor White
Write-Host ""
Write-Host "💡 Visit your app at the URL above!" -ForegroundColor Yellow
Write-Host ""
Write-Host "To view logs:" -ForegroundColor Cyan
Write-Host "az containerapp logs show --name $($outputs.containerAppName.value) --resource-group $ResourceGroupName --follow" -ForegroundColor Gray
Write-Host ""

# Save complete outputs
$allOutputs = @{
    infra = $infraOutputs
    app = $outputs
}
$allOutputsFile = Join-Path $PSScriptRoot "deployment-outputs.json"
$allOutputs | ConvertTo-Json -Depth 10 | Set-Content $allOutputsFile
Write-Host "💾 All outputs saved to: deployment-outputs.json" -ForegroundColor Green
Write-Host ""
