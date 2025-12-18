# Docker Image Setting
## Build image
```yaml
# Container working in background (nginx server)
podman container run -d -p 5566:80 nginx:alpine
# Curl the html content from nginx default page
curl localhost:5566
# Show all the working container
podman container ls
# Enter to the container
podman container exec -it {container id} ash
```