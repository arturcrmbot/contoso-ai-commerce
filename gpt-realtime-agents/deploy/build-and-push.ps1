#!/usr/bin/env pwsh
# Build and Push Docker image to Azure Container Registry

param(
    [Parameter(Mandatory=$false)]
    [string]$ImageTag = "latest",

    [Parameter(Mandatory=$false)]
    [string]$ResourceGroupName = "rg-contosoaicommerce"
)

$ErrorActionPreference = "Stop"

Write-Host "🐳 Contoso AI Commerce - Docker Build & Push" -ForegroundColor Cyan
Write-Host "=============================================" -ForegroundColor Cyan
Write-Host ""

# Check if deployment outputs exist
$outputsFile = Join-Path $PSScriptRoot "deployment-outputs.json"
if (-not (Test-Path $outputsFile)) {
    Write-Host "❌ Deployment outputs not found. Please run './deploy.ps1' first." -ForegroundColor Red
    exit 1
}

$outputs = Get-Content $outputsFile | ConvertFrom-Json
$acrName = $outputs.acrName.value
$acrLoginServer = $outputs.acrLoginServer.value

Write-Host "📋 Using ACR: $acrLoginServer" -ForegroundColor Yellow
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

# Update Container App to use new image
Write-Host "🔄 Updating Container App with new image..." -ForegroundColor Yellow
$containerAppName = $outputs.containerAppName.value

az containerapp update `
    --name $containerAppName `
    --resource-group $ResourceGroupName `
    --image $fullImageName `
    --output none

if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Failed to update Container App" -ForegroundColor Red
    exit 1
}
Write-Host "✅ Container App updated" -ForegroundColor Green
Write-Host ""

Write-Host "🎉 Build and Deployment Complete!" -ForegroundColor Green
Write-Host ""
Write-Host "Your app is now running at:" -ForegroundColor Cyan
Write-Host "$($outputs.containerAppUrl.value)" -ForegroundColor White
Write-Host ""
Write-Host "To view logs, run:" -ForegroundColor Cyan
Write-Host "az containerapp logs show --name $containerAppName --resource-group $ResourceGroupName --follow" -ForegroundColor Gray
Write-Host ""
