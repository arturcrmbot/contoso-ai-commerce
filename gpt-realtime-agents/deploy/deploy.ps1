#!/usr/bin/env pwsh
# Single Unified Deployment Script
# - First run: Deploys infrastructure + builds and deploys app
# - Subsequent runs: Quick rebuild and update

param(
    [Parameter(Mandatory=$false)]
    [string]$ResourceGroupName = "rg-contosoaicommerce",

    [Parameter(Mandatory=$false)]
    [string]$Location = "eastus2",

    [Parameter(Mandatory=$false)]
    [switch]$Force
)

$ErrorActionPreference = "Stop"

Write-Host ""
Write-Host "╔════════════════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║                                                            ║" -ForegroundColor Cyan
Write-Host "║         🚀 Travel Agent - Deploy 🚀                       ║" -ForegroundColor Cyan
Write-Host "║                                                            ║" -ForegroundColor Cyan
Write-Host "╚════════════════════════════════════════════════════════════╝" -ForegroundColor Cyan
Write-Host ""

# Determine deployment mode
$outputsFile = Join-Path $PSScriptRoot "deployment-outputs.json"
$isFirstDeploy = -not (Test-Path $outputsFile) -or $Force

if ($isFirstDeploy) {
    Write-Host "🆕 First-time deployment detected" -ForegroundColor Magenta
    Write-Host ""
} else {
    Write-Host "🔄 Existing deployment detected - will update app only" -ForegroundColor Magenta
    Write-Host ""
}

# Check Azure login
Write-Host "📋 Checking Azure login..." -ForegroundColor Yellow
$account = az account show 2>$null | ConvertFrom-Json
if (-not $account) {
    Write-Host "❌ Not logged in to Azure. Please run 'az login' first." -ForegroundColor Red
    exit 1
}
Write-Host "✅ Logged in as: $($account.user.name)" -ForegroundColor Green
Write-Host "✅ Subscription: $($account.name)" -ForegroundColor Green
Write-Host ""

# Navigate to project root
$projectRoot = Split-Path $PSScriptRoot -Parent
Set-Location $projectRoot

# ============================================================================
# FIRST-TIME DEPLOYMENT
# ============================================================================
if ($isFirstDeploy) {
    Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Cyan
    Write-Host "PHASE 1: INFRASTRUCTURE SETUP" -ForegroundColor Cyan
    Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Cyan
    Write-Host ""

    # Create resource group
    Write-Host "📦 Creating resource group: $ResourceGroupName..." -ForegroundColor Yellow
    az group create --name $ResourceGroupName --location $Location --output none
    if ($LASTEXITCODE -ne 0) {
        Write-Host "❌ Failed to create resource group" -ForegroundColor Red
        exit 1
    }
    Write-Host "✅ Resource group created" -ForegroundColor Green
    Write-Host ""

    # Deploy infrastructure
    Write-Host "🏗️  Deploying ACR and Container Apps Environment..." -ForegroundColor Yellow
    $deploymentName = "travelagent-infra-$(Get-Date -Format 'yyyyMMdd-HHmmss')"

    Set-Location $PSScriptRoot
    $infraDeployment = az deployment group create `
        --name $deploymentName `
        --resource-group $ResourceGroupName `
        --template-file main-infra-only.bicep `
        --parameters location=$Location `
        --output json | ConvertFrom-Json

    if ($LASTEXITCODE -ne 0) {
        Write-Host "❌ Infrastructure deployment failed" -ForegroundColor Red
        exit 1
    }

    $infraOutputs = $infraDeployment.properties.outputs
    Write-Host "✅ Infrastructure deployed" -ForegroundColor Green
    Write-Host ""

    Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Cyan
    Write-Host "PHASE 2: APPLICATION BUILD & DEPLOY" -ForegroundColor Cyan
    Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Cyan
    Write-Host ""

    $acrName = $infraOutputs.acrName.value
    $acrLoginServer = $infraOutputs.acrLoginServer.value
    $acrUsername = $infraOutputs.acrUsername.value
    $acrPassword = $infraOutputs.acrPassword.value
    $containerEnvId = $infraOutputs.containerEnvId.value
    $imageTag = Get-Date -Format "yyyyMMdd-HHmmss"

    # Login to ACR
    Write-Host "🔐 Logging in to Azure Container Registry..." -ForegroundColor Yellow

    # Check if Docker is running
    $dockerRunning = $false
    try {
        docker info 2>&1 | Out-Null
        if ($LASTEXITCODE -eq 0) {
            $dockerRunning = $true
        }
    } catch {
        $dockerRunning = $false
    }

    if (-not $dockerRunning) {
        Write-Host "⚠️  Docker Desktop is not running!" -ForegroundColor Red
        Write-Host ""
        Write-Host "Please:" -ForegroundColor Yellow
        Write-Host "1. Start Docker Desktop" -ForegroundColor White
        Write-Host "2. Wait for it to fully start" -ForegroundColor White
        Write-Host "3. Run this script again" -ForegroundColor White
        exit 1
    }

    az acr login --name $acrName 2>&1 | Out-Null
    if ($LASTEXITCODE -ne 0) {
        Write-Host "❌ Failed to login to ACR" -ForegroundColor Red
        exit 1
    }
    Write-Host "✅ Logged in to ACR" -ForegroundColor Green
    Write-Host ""

    # Build Docker image
    Set-Location $projectRoot
    $imageName = "travelagent"
    $fullImageName = "${acrLoginServer}/${imageName}:${imageTag}"

    Write-Host "🏗️  Building Docker image..." -ForegroundColor Yellow
    Write-Host "   $fullImageName" -ForegroundColor Gray
    docker build -t $fullImageName -f Dockerfile . 2>&1 | ForEach-Object {
        if ($_ -match "^Step \d+/\d+|^Successfully built|^Successfully tagged") {
            Write-Host "   $_" -ForegroundColor Gray
        }
    }
    if ($LASTEXITCODE -ne 0) {
        Write-Host "❌ Docker build failed" -ForegroundColor Red
        exit 1
    }
    Write-Host "✅ Docker image built" -ForegroundColor Green
    Write-Host ""

    # Push to ACR
    Write-Host "☁️  Pushing image to ACR..." -ForegroundColor Yellow
    docker push $fullImageName 2>&1 | ForEach-Object {
        if ($_ -match "digest:|Pushed|latest:") {
            Write-Host "   $_" -ForegroundColor Gray
        }
    }
    if ($LASTEXITCODE -ne 0) {
        Write-Host "❌ Docker push failed" -ForegroundColor Red
        exit 1
    }
    Write-Host "✅ Image pushed" -ForegroundColor Green
    Write-Host ""

    # Read .env file
    Write-Host "📄 Reading environment configuration..." -ForegroundColor Yellow
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
    Write-Host "✅ Configuration loaded" -ForegroundColor Green
    Write-Host ""

    # Deploy Container App
    Write-Host "🚀 Creating Container App..." -ForegroundColor Yellow
    $appDeploymentName = "travelagent-app-$(Get-Date -Format 'yyyyMMdd-HHmmss')"

    Set-Location $PSScriptRoot
    $appDeployment = az deployment group create `
        --name $appDeploymentName `
        --resource-group $ResourceGroupName `
        --template-file main-app-only.bicep `
        --parameters `
            location=$Location `
            imageTag=$imageTag `
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
        Write-Host "❌ Container App deployment failed" -ForegroundColor Red
        exit 1
    }

    $appOutputs = $appDeployment.properties.outputs
    Write-Host "✅ Container App deployed" -ForegroundColor Green
    Write-Host ""

    # Assign Cognitive Services OpenAI User role to the Container App's managed identity
    Write-Host "🔐 Configuring role-based authentication..." -ForegroundColor Yellow
    $principalId = $appOutputs.containerAppPrincipalId.value

    # Extract Azure OpenAI resource info from the URL (e.g., https://arzie-mhj8yuwb-eastus2.openai.azure.com/...)
    $realtimeUrl = $envVars['AZURE_GPT_REALTIME_URL']
    if ($realtimeUrl -match 'https://([^.]+)\.openai\.azure\.com') {
        $openAiResourceName = $matches[1]
        Write-Host "   OpenAI Resource: $openAiResourceName" -ForegroundColor Gray
        Write-Host "   Principal ID: $principalId" -ForegroundColor Gray

        # Find the OpenAI resource ID
        $openAiResources = az cognitiveservices account list --query "[?contains(name, '$openAiResourceName')]" --output json | ConvertFrom-Json
        if ($openAiResources -and $openAiResources.Count -gt 0) {
            $openAiResourceId = $openAiResources[0].id
            Write-Host "   Resource ID: $openAiResourceId" -ForegroundColor Gray

            # Assign the role
            Write-Host "   Assigning 'Cognitive Services OpenAI User' role..." -ForegroundColor Gray
            az role assignment create `
                --role "Cognitive Services OpenAI User" `
                --assignee-object-id $principalId `
                --assignee-principal-type ServicePrincipal `
                --scope $openAiResourceId `
                --output none 2>&1 | Out-Null

            if ($LASTEXITCODE -eq 0) {
                Write-Host "✅ Role assigned successfully" -ForegroundColor Green
            } else {
                Write-Host "⚠️  Role assignment may have failed or already exists" -ForegroundColor Yellow
            }
        } else {
            Write-Host "⚠️  Could not find Azure OpenAI resource. You may need to assign the role manually:" -ForegroundColor Yellow
            Write-Host "   az role assignment create --role 'Cognitive Services OpenAI User' --assignee-object-id $principalId --scope <your-openai-resource-id>" -ForegroundColor Gray
        }
    } else {
        Write-Host "⚠️  Could not parse OpenAI resource from URL. Manual role assignment required." -ForegroundColor Yellow
    }
    Write-Host ""

    # Save outputs
    $allOutputs = @{
        infra = $infraOutputs
        app = $appOutputs
    }
    $allOutputs | ConvertTo-Json -Depth 10 | Set-Content $outputsFile

# ============================================================================
# UPDATE EXISTING DEPLOYMENT
# ============================================================================
} else {
    Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Cyan
    Write-Host "QUICK UPDATE" -ForegroundColor Cyan
    Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Cyan
    Write-Host ""

    # Load existing outputs
    $outputs = Get-Content $outputsFile | ConvertFrom-Json
    $acrName = $outputs.infra.acrName.value
    $acrLoginServer = $outputs.infra.acrLoginServer.value
    $containerAppName = $outputs.app.containerAppName.value
    $imageTag = Get-Date -Format "yyyyMMdd-HHmmss"

    Write-Host "📋 Target: $containerAppName" -ForegroundColor Gray
    Write-Host ""

    # Check if Docker is running
    Write-Host "🐳 Checking Docker..." -ForegroundColor Yellow
    $dockerRunning = $false
    try {
        docker info 2>&1 | Out-Null
        if ($LASTEXITCODE -eq 0) {
            $dockerRunning = $true
        }
    } catch {
        $dockerRunning = $false
    }

    if (-not $dockerRunning) {
        Write-Host "⚠️  Docker Desktop is not running!" -ForegroundColor Red
        Write-Host ""
        Write-Host "Please:" -ForegroundColor Yellow
        Write-Host "1. Start Docker Desktop" -ForegroundColor White
        Write-Host "2. Wait for it to fully start" -ForegroundColor White
        Write-Host "3. Run this script again" -ForegroundColor White
        exit 1
    }

    # Login to ACR
    az acr login --name $acrName 2>&1 | Out-Null
    if ($LASTEXITCODE -ne 0) {
        Write-Host "❌ Failed to login to ACR" -ForegroundColor Red
        exit 1
    }
    Write-Host "✅ Docker ready" -ForegroundColor Green
    Write-Host ""

    # Build Docker image
    Set-Location $projectRoot
    $imageName = "travelagent"
    $fullImageName = "${acrLoginServer}/${imageName}:${imageTag}"

    Write-Host "🏗️  Building Docker image..." -ForegroundColor Yellow
    docker build -t $fullImageName -f Dockerfile . 2>&1 | ForEach-Object {
        if ($_ -match "^Step \d+/\d+|^Successfully built|^Successfully tagged") {
            Write-Host "   $_" -ForegroundColor Gray
        }
    }
    if ($LASTEXITCODE -ne 0) {
        Write-Host "❌ Docker build failed" -ForegroundColor Red
        exit 1
    }
    Write-Host "✅ Image built" -ForegroundColor Green
    Write-Host ""

    # Push to ACR
    Write-Host "☁️  Pushing to ACR..." -ForegroundColor Yellow
    docker push $fullImageName 2>&1 | ForEach-Object {
        if ($_ -match "digest:|Pushed|latest:") {
            Write-Host "   $_" -ForegroundColor Gray
        }
    }
    if ($LASTEXITCODE -ne 0) {
        Write-Host "❌ Push failed" -ForegroundColor Red
        exit 1
    }
    Write-Host "✅ Image pushed" -ForegroundColor Green
    Write-Host ""

    # Update Container App
    Write-Host "🚀 Updating Container App..." -ForegroundColor Yellow
    az containerapp update `
        --name $containerAppName `
        --resource-group $ResourceGroupName `
        --image $fullImageName `
        --output none

    if ($LASTEXITCODE -ne 0) {
        Write-Host "❌ Update failed" -ForegroundColor Red
        exit 1
    }
    Write-Host "✅ Container App updated" -ForegroundColor Green
    Write-Host ""

    # Wait for revision
    Write-Host "⏳ Waiting for new revision..." -ForegroundColor Yellow
    $maxAttempts = 30
    $attempt = 0
    $revisionReady = $false

    while ($attempt -lt $maxAttempts -and -not $revisionReady) {
        $attempt++
        Start-Sleep -Seconds 2

        $revisions = az containerapp revision list `
            --name $containerAppName `
            --resource-group $ResourceGroupName `
            --output json | ConvertFrom-Json

        $latestRevision = $revisions | Sort-Object -Property createdTime -Descending | Select-Object -First 1

        if ($latestRevision.properties.provisioningState -eq "Provisioned" -and
            $latestRevision.properties.runningState -eq "Running") {
            $revisionReady = $true
            Write-Host "✅ Revision ready: $($latestRevision.name)" -ForegroundColor Green
        } else {
            Write-Host "   Status: $($latestRevision.properties.provisioningState)/$($latestRevision.properties.runningState)" -ForegroundColor Gray
        }
    }

    if (-not $revisionReady) {
        Write-Host "⚠️  Revision taking longer than expected, but update was applied" -ForegroundColor Yellow
    }
    Write-Host ""

    $appOutputs = $outputs.app
}

# ============================================================================
# FINAL OUTPUT
# ============================================================================
Write-Host "╔════════════════════════════════════════════════════════════╗" -ForegroundColor Green
Write-Host "║                                                            ║" -ForegroundColor Green
Write-Host "║                  ✅ SUCCESS! ✅                            ║" -ForegroundColor Green
Write-Host "║                                                            ║" -ForegroundColor Green
Write-Host "╚════════════════════════════════════════════════════════════╝" -ForegroundColor Green
Write-Host ""

Write-Host "🎯 Your Application:" -ForegroundColor Cyan
Write-Host "   URL: $($appOutputs.containerAppUrl.value)" -ForegroundColor White
Write-Host ""

Write-Host "💡 Tips:" -ForegroundColor Yellow
Write-Host "   • Changes may take 30-60 seconds to propagate" -ForegroundColor Gray
Write-Host "   • Hard refresh browser (Ctrl+F5) to see latest" -ForegroundColor Gray
Write-Host "   • Run './deploy.ps1' anytime to update the app" -ForegroundColor Gray
Write-Host ""
