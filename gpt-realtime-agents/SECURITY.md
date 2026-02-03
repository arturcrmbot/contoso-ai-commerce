# Security Guidelines

This document outlines security best practices for deploying and using the Contoso AI Commerce application.

## Before Making This Repository Public

### Critical Security Checks

- [x] **Secrets Management**: Ensure no API keys, passwords, or secrets are committed to the repository
- [x] **Environment Variables**: All sensitive configuration is handled via environment variables
- [x] **Docker Security**: `.env` files are excluded from Docker images via `.dockerignore`
- [x] **Parameters Files**: Deployment parameter files with secrets are gitignored

## Handling Secrets

### DO NOT commit secrets to the repository

Never commit the following files with real credentials:
- `.env` files (use `.env.sample` as template)
- `main.parameters.json` (use `main.parameters.sample.json` as template)
- Any file containing API keys, passwords, or connection strings

### Using Environment Variables

1. **Local Development**: 
   ```bash
   cp .env.sample .env
   # Edit .env with your actual credentials
   ```

2. **Docker Deployment**:
   ```bash
   docker run --env-file .env contoso-ai-commerce
   ```

3. **Azure Container Apps**:
   - Store secrets in Azure Key Vault
   - Reference secrets via environment variables in Container Apps configuration
   - Never pass secrets via command-line arguments

### Azure OpenAI Credentials

The application supports two authentication methods:

1. **API Key** (Development/Testing):
   - Set `AZURE_GPT_REALTIME_KEY` environment variable
   - Key is never logged or exposed in responses

2. **Managed Identity** (Production - Recommended):
   - Leave `AZURE_GPT_REALTIME_KEY` empty
   - Configure Azure Managed Identity for your Container App
   - Grant the identity appropriate permissions to Azure OpenAI

## Production Security Checklist

### CORS Configuration

The default CORS configuration allows all origins (`allow_origins=["*"]`). **This is insecure for production.**

Update `audio_backend/backend.py`:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://yourdomain.com"],  # Replace with your domain
    allow_credentials=True,
    allow_methods=["GET", "POST"],  # Only allow needed methods
    allow_headers=["Content-Type", "Authorization"],  # Only allow needed headers
)
```

### Network Security

1. **Use HTTPS Only**: Ensure your deployment uses HTTPS/TLS encryption
2. **Restrict Origins**: Configure CORS to only allow your frontend domain
3. **API Rate Limiting**: Consider implementing rate limiting for production
4. **Input Validation**: The application validates function call inputs, but review for your use case

### Container Security

1. **Non-Root User**: Consider running the container as a non-root user
2. **Read-Only Filesystem**: Where possible, use read-only file systems
3. **Minimize Image Size**: The multi-stage Dockerfile already minimizes the final image
4. **Regular Updates**: Keep base images and dependencies updated

### Dependency Security

Run security audits regularly:

```bash
# Python dependencies
pip install safety
safety check

# Node.js dependencies
npm audit
```

### Azure Security Best Practices

1. **Use Managed Identities**: Avoid using API keys in production
2. **Private Endpoints**: Use Azure Private Link for Azure OpenAI connections
3. **Network Security Groups**: Restrict network access to your resources
4. **Monitor and Alert**: Set up Azure Monitor alerts for suspicious activity
5. **Enable Logging**: Enable diagnostic logging for audit trails

## Reporting Security Issues

If you discover a security vulnerability, please report it responsibly:

1. **Do NOT** open a public GitHub issue
2. Contact the repository maintainers privately
3. Provide detailed information about the vulnerability
4. Allow time for the issue to be fixed before public disclosure

## Additional Resources

- [Azure OpenAI Service Security](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/managed-identity)
- [FastAPI Security Best Practices](https://fastapi.tiangolo.com/tutorial/security/)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [Docker Security Best Practices](https://docs.docker.com/develop/security-best-practices/)
