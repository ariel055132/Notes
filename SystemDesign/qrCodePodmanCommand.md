# Commands
```txt
1. View Podman container Logs
podman logs -f qr-api

2. Stop and remove Podman container 
podman stop qr-api && podman rm qr-api

3. Rebuild the Podman images
podman build -t qr-code-generator

4. Start a new Container
podman run -d --name qr-api -p 8000:8000 -v qr-data:/data:Z qr-code-generator
```

# Test
```
curl http://localhost:8000/docs
```