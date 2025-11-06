#!/usr/bin/env pwsh
# Fixed two-step deployment: Infrastructure first, then build and deploy app

param(
    [Parameter(Mandatory=$false)]
    [string]$ResourceGroupName = "rg-contosoaicommerce",

    [Parameter(Mandatory=$false)]
    [string]$Location = "eastus2",

    [Parameter(Mandatory=$false)]
    [string]$ImageTag = "latest"
)

$ErrorActionPreference = "Stop"

Write-Host ""
Write-Host "╔════════════════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║                                                            ║" -ForegroundColor Cyan
Write-Host "║         🚀 Contoso AI Commerce - Full Deployment 🚀       ║" -ForegroundColor Cyan
Write-Host "║                                                            ║" -ForegroundColor Cyan
Write-Host "╚════════════════════════════════════════════════════════════╝" -ForegroundColor Cyan
Write-Host ""

# Step 1: Deploy Infrastructure Only
Write-Host "📦 STEP 1/2: Deploying Infrastructure (ACR + Environment)..." -ForegroundColor Magenta
Write-Host ""
& "$PSScriptRoot/deploy-infra-only.ps1" -ResourceGroupName $ResourceGroupName -Location $Location
if ($LASTEXITCODE -ne 0) {
    Write-Host ""
    Write-Host "❌ Infrastructure deployment failed. Aborting." -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "─────────────────────────────────────────────────────────────" -ForegroundColor Gray
Write-Host ""

# Step 2: Build and Deploy App
Write-Host "🐳 STEP 2/2: Building Image & Deploying Container App..." -ForegroundColor Magenta
Write-Host ""
& "$PSScriptRoot/build-and-deploy-app.ps1" -ImageTag $ImageTag -ResourceGroupName $ResourceGroupName
if ($LASTEXITCODE -ne 0) {
    Write-Host ""
    Write-Host "❌ Build and deploy failed." -ForegroundColor Red
    exit 1
}

# Final success message
Write-Host ""
Write-Host "╔════════════════════════════════════════════════════════════╗" -ForegroundColor Green
Write-Host "║                                                            ║" -ForegroundColor Green
Write-Host "║              ✅ DEPLOYMENT SUCCESSFUL! ✅                  ║" -ForegroundColor Green
Write-Host "║                                                            ║" -ForegroundColor Green
Write-Host "╚════════════════════════════════════════════════════════════╝" -ForegroundColor Green
Write-Host ""

# Load outputs and display summary
$outputs = Get-Content "$PSScriptRoot/deployment-outputs.json" | ConvertFrom-Json
Write-Host "🎯 Your Application:" -ForegroundColor Cyan
Write-Host "   App URL: $($outputs.app.containerAppUrl.value)" -ForegroundColor White
Write-Host ""
Write-Host "📊 Management:" -ForegroundColor Cyan
Write-Host "   Resource Group: $ResourceGroupName" -ForegroundColor White
Write-Host "   Container App: $($outputs.app.containerAppName.value)" -ForegroundColor White
Write-Host "   Container Registry: $($outputs.infra.acrName.value)" -ForegroundColor White
Write-Host ""
Write-Host "💡 Tip: Bookmark your app URL to access it anytime!" -ForegroundColor Yellow
Write-Host ""
