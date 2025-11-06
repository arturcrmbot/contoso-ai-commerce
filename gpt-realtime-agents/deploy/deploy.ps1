#!/usr/bin/env pwsh
# Deployment script for Contoso AI Commerce
# This script deploys the infrastructure to Azure

param(
    [Parameter(Mandatory=$false)]
    [string]$ResourceGroupName = "rg-contosoaicommerce",

    [Parameter(Mandatory=$false)]
    [string]$Location = "eastus2",

    [Parameter(Mandatory=$false)]
    [string]$ParametersFile = "main.parameters.json"
)

$ErrorActionPreference = "Stop"

Write-Host "🚀 Contoso AI Commerce - Azure Deployment" -ForegroundColor Cyan
Write-Host "=========================================" -ForegroundColor Cyan
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

# Deploy Bicep template
Write-Host "🏗️  Deploying infrastructure (this may take 3-5 minutes)..." -ForegroundColor Yellow
$deploymentName = "contosoaicommerce-$(Get-Date -Format 'yyyyMMdd-HHmmss')"

$deployment = az deployment group create `
    --name $deploymentName `
    --resource-group $ResourceGroupName `
    --template-file main.bicep `
    --parameters $ParametersFile `
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
Write-Host "=========================================" -ForegroundColor Cyan
Write-Host "ACR Login Server: $($outputs.acrLoginServer.value)" -ForegroundColor White
Write-Host "ACR Name: $($outputs.acrName.value)" -ForegroundColor White
Write-Host "ACR Username: $($outputs.acrUsername.value)" -ForegroundColor White
Write-Host "Container App Name: $($outputs.containerAppName.value)" -ForegroundColor White
Write-Host "Container App URL: $($outputs.containerAppUrl.value)" -ForegroundColor White
Write-Host "Resource Group: $($outputs.resourceGroupName.value)" -ForegroundColor White
Write-Host ""

# Save outputs to file for build script
$outputsFile = Join-Path $PSScriptRoot "deployment-outputs.json"
$outputs | ConvertTo-Json -Depth 10 | Set-Content $outputsFile
Write-Host "💾 Outputs saved to: $outputsFile" -ForegroundColor Green
Write-Host ""

Write-Host "🎉 Deployment Complete!" -ForegroundColor Green
Write-Host ""
Write-Host "Next Steps:" -ForegroundColor Cyan
Write-Host "1. Run './build-and-push.ps1' to build and push your Docker image" -ForegroundColor White
Write-Host "2. Visit your app at: $($outputs.containerAppUrl.value)" -ForegroundColor White
Write-Host ""
