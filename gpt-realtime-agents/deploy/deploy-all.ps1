#!/usr/bin/env pwsh
# One-command deployment: Infrastructure + Build + Push

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

# Step 1: Deploy Infrastructure
Write-Host "📦 STEP 1/2: Deploying Infrastructure..." -ForegroundColor Magenta
Write-Host ""
& "$PSScriptRoot/deploy.ps1" -ResourceGroupName $ResourceGroupName -Location $Location
if ($LASTEXITCODE -ne 0) {
    Write-Host ""
    Write-Host "❌ Infrastructure deployment failed. Aborting." -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "─────────────────────────────────────────────────────────────" -ForegroundColor Gray
Write-Host ""

# Step 2: Build and Push
Write-Host "🐳 STEP 2/2: Building & Deploying Application..." -ForegroundColor Magenta
Write-Host ""
& "$PSScriptRoot/build-and-push.ps1" -ImageTag $ImageTag -ResourceGroupName $ResourceGroupName
if ($LASTEXITCODE -ne 0) {
    Write-Host ""
    Write-Host "❌ Build and push failed. Infrastructure was deployed but app is not running." -ForegroundColor Red
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
Write-Host "🎯 Quick Access:" -ForegroundColor Cyan
Write-Host "   App URL: $($outputs.containerAppUrl.value)" -ForegroundColor White
Write-Host ""
Write-Host "📊 Management:" -ForegroundColor Cyan
Write-Host "   Resource Group: $ResourceGroupName" -ForegroundColor White
Write-Host "   Container App: $($outputs.containerAppName.value)" -ForegroundColor White
Write-Host "   Container Registry: $($outputs.acrName.value)" -ForegroundColor White
Write-Host ""
Write-Host "💡 Tip: Bookmark your app URL to access it anytime!" -ForegroundColor Yellow
Write-Host ""
