#!/usr/bin/env pwsh
# Deploy only ACR and Container Apps Environment (no Container App yet)

param(
    [Parameter(Mandatory=$false)]
    [string]$ResourceGroupName = "rg-contosoaicommerce",

    [Parameter(Mandatory=$false)]
    [string]$Location = "eastus2"
)

$ErrorActionPreference = "Stop"

Write-Host "🚀 Contoso AI Commerce - Infrastructure Only" -ForegroundColor Cyan
Write-Host "=============================================" -ForegroundColor Cyan
Write-Host ""

# Check if logged in to Azure
Write-Host "📋 Checking Azure login..." -ForegroundColor Yellow
$account = az account show 2>$null | ConvertFrom-Json
if (-not $account) {
    Write-Host "❌ Not logged in to Azure. Please run 'az login' first." -ForegroundColor Red
    exit 1
}
Write-Host "✅ Logged in as: $($account.user.name)" -ForegroundColor Green
Write-Host "✅ Subscription: $($account.name) ($($account.id))" -ForegroundColor Green
Write-Host ""

# Create resource group
Write-Host "📦 Creating resource group: $ResourceGroupName in $Location..." -ForegroundColor Yellow
az group create --name $ResourceGroupName --location $Location --output none
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Failed to create resource group" -ForegroundColor Red
    exit 1
}
Write-Host "✅ Resource group created" -ForegroundColor Green
Write-Host ""

# Deploy infrastructure (ACR + Environment only)
Write-Host "🏗️  Deploying ACR and Container Apps Environment..." -ForegroundColor Yellow
$deploymentName = "contoso-infra-$(Get-Date -Format 'yyyyMMdd-HHmmss')"

$deployment = az deployment group create `
    --name $deploymentName `
    --resource-group $ResourceGroupName `
    --template-file main-infra-only.bicep `
    --parameters location=$Location `
    --output json | ConvertFrom-Json

if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Deployment failed" -ForegroundColor Red
    exit 1
}

Write-Host "✅ Infrastructure deployed successfully!" -ForegroundColor Green
Write-Host ""

# Extract outputs
$outputs = $deployment.properties.outputs

Write-Host "📊 Deployment Outputs:" -ForegroundColor Cyan
Write-Host "=====================================" -ForegroundColor Cyan
Write-Host "ACR Login Server: $($outputs.acrLoginServer.value)" -ForegroundColor White
Write-Host "ACR Name: $($outputs.acrName.value)" -ForegroundColor White
Write-Host "Container Environment: $($outputs.containerEnvName.value)" -ForegroundColor White
Write-Host ""

# Save outputs to file
$outputsFile = Join-Path $PSScriptRoot "infra-outputs.json"
$outputs | ConvertTo-Json -Depth 10 | Set-Content $outputsFile
Write-Host "💾 Outputs saved to: $outputsFile" -ForegroundColor Green
Write-Host ""

Write-Host "✅ Step 1 Complete!" -ForegroundColor Green
Write-Host ""
Write-Host "Next: Run './build-and-deploy-app.ps1' to build image and create Container App" -ForegroundColor Cyan
Write-Host ""
