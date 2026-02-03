# Azure Container Apps Deployment

Deploy Contoso AI Commerce to Azure Container Apps using simplified Bicep templates.

## What Gets Deployed

1. Azure Container Registry (ACR) - Stores Docker images
2. Log Analytics Workspace - Monitoring and logs
3. Container Apps Environment - Hosting platform
4. Container App - Your application

**Estimated Monthly Cost:** $20-40 (East US 2)

## Prerequisites

- Azure CLI installed and logged in
- Docker Desktop running
- `.env` file configured with Azure OpenAI credentials (copy from `.env.sample`)
- PowerShell (Windows) or pwsh (Linux/Mac)

> **⚠️ Security Note**: Never commit `.env` or `main.parameters.json` with real credentials. Use `main.parameters.sample.json` as a template and copy it to `main.parameters.json` with your actual values.

## Deployment Steps

### Option 1: Full Deployment (Recommended)

```powershell
cd deploy
.\deploy-all-fixed.ps1
```

This runs both infrastructure and application deployment automatically.

**Time:** ~15 minutes

### Option 2: Manual Step-by-Step

**Step 1: Deploy Infrastructure**
```powershell
.\deploy-infra-only.ps1
```

Creates ACR and Container Apps Environment. Takes ~3-5 minutes.

**Step 2: Build and Deploy Application**
```powershell
.\build-and-deploy-app.ps1
```

Builds Docker image, pushes to ACR, creates Container App. Takes ~10-15 minutes.

## Configuration

### Resource Group

Default: `rg-contosoaicommerce` in `eastus2`

To customize:
```powershell
.\deploy-all-fixed.ps1 -ResourceGroupName "my-rg" -Location "westus2"
```

### Environment Variables

The deployment reads from your `.env` file:
- `AZURE_GPT_REALTIME_URL`
- `WEBRTC_URL`
- `AZURE_GPT_REALTIME_KEY`
- `AZURE_GPT_REALTIME_DEPLOYMENT`
- `AZURE_GPT_REALTIME_VOICE`

### Container Resources

Edit `main-app-only.bicep` to change:
- CPU: Default 1.0 cores
- Memory: Default 2GB
- Min replicas: Default 1
- Max replicas: Default 3

## Post-Deployment

### Get Application URL

```powershell
$outputs = Get-Content deployment-outputs.json | ConvertFrom-Json
$outputs.app.containerAppUrl.value
```

### View Logs

```powershell
$appName = (Get-Content deployment-outputs.json | ConvertFrom-Json).app.containerAppName.value
az containerapp logs show --name $appName --resource-group rg-contosoaicommerce --follow
```

### Restart Application

```powershell
az containerapp revision restart --name $appName --resource-group rg-contosoaicommerce
```

### Redeploy After Code Changes

```powershell
.\build-and-deploy-app.ps1
```

This rebuilds the Docker image and updates the Container App.

## Troubleshooting

### Deployment Fails with "Container App name too long"

The base name is too long. This is fixed in current templates (uses `contoso` instead of `contosoaicommerce`).

### "Image not found" Error

The deployment tries to create the Container App before the image is pushed. Use the fixed deployment:
```powershell
.\deploy-all-fixed.ps1
```

### Docker Build Fails

- Verify Docker Desktop is running
- Check you're in the `deploy/` directory when running scripts
- Ensure `.env` file exists in project root

### ACR Login Fails

```powershell
$acrName = (Get-Content infra-outputs.json | ConvertFrom-Json).acrName.value
az acr login --name $acrName
```

### Container App Won't Start

Check logs for errors:
```powershell
az containerapp logs show --name $appName --resource-group rg-contosoaicommerce --tail 100
```

Common issues:
- Missing environment variables
- Invalid Azure OpenAI credentials
- Port mismatch (app must listen on 8080)

## File Structure

```
deploy/
├── main-infra-only.bicep       # ACR + Environment
├── main-app-only.bicep         # Container App
├── deploy-infra-only.ps1       # Deploy infrastructure
├── build-and-deploy-app.ps1    # Build and deploy app
├── deploy-all-fixed.ps1        # Full deployment
├── infra-outputs.json          # Generated after step 1
├── deployment-outputs.json     # Generated after step 2
└── README.md                   # This file
```

## Clean Up

Delete all resources:
```powershell
az group delete --name rg-contosoaicommerce --yes
```

## Old Deployment Files (Not Used)

These files are not used by the current deployment:
- `main.bicep` - Old single-step deployment (has chicken-egg problem)
- `main.parameters.json` - Old parameters file
- `deploy.ps1` - Old deployment script
- `build-and-push.ps1` - Old build script
- `deploy-all.ps1` - Old combined script

Use the `-fixed` versions instead.
