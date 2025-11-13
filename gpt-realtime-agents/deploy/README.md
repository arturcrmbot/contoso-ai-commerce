# Azure Container Apps Deployment

Deploy Contoso AI Commerce to Azure Container Apps with a single command.

## What Gets Deployed

1. Azure Container Registry (ACR) - Stores Docker images
2. Log Analytics Workspace - Monitoring and logs
3. Container Apps Environment - Hosting platform
4. Container App - Your application

**Estimated Monthly Cost:** $20-40 (East US 2)

## Prerequisites

- Azure CLI installed and logged in (`az login`)
- Docker Desktop running
- `.env` file configured with Azure OpenAI credentials
- PowerShell (Windows) or pwsh (Linux/Mac)

## Deployment

### One Command Deployment

```powershell
cd deploy
.\deploy.ps1
```

**First run:** Deploys infrastructure + builds and deploys app (~15 minutes)
**Subsequent runs:** Quick rebuild and update (~5 minutes)

The script automatically detects if infrastructure exists and runs the appropriate workflow.

### Custom Configuration

```powershell
.\deploy.ps1 -ResourceGroupName "my-rg" -Location "westus2"
```

### Force Full Redeployment

```powershell
.\deploy.ps1 -Force
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

### Update After Code Changes

```powershell
.\deploy.ps1
```

The script detects existing infrastructure and performs a quick update.

## Troubleshooting

### Docker Desktop Not Running

The script will detect this and prompt you to start Docker Desktop before continuing.

### Docker Build Fails

- Verify Docker Desktop is running
- Ensure `.env` file exists in project root
- Check Docker has enough resources allocated

### ACR Login Fails

```powershell
$acrName = (Get-Content deployment-outputs.json | ConvertFrom-Json).infra.acrName.value
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
├── deploy.ps1                  # Single unified deployment script
├── main-infra-only.bicep       # Bicep: ACR + Environment
├── main-app-only.bicep         # Bicep: Container App
├── main.bicep                  # Bicep: Legacy (not used)
├── main.parameters.json        # Legacy parameters (not used)
├── deployment-outputs.json     # Generated deployment info
└── README.md                   # This file
```

## Clean Up

Delete all resources:
```powershell
az group delete --name rg-contosoaicommerce --yes
```
