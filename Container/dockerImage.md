# Docker Image Setting
## Build image
```yaml
# Container working in background (nginx server)
podman container run -d -p 5566:80 nginx:alpine
# Curl the html content from nginx default page
curl localhost:5566
# Besides curl, can type the website to show the html content
http://localhost:5566/
# Show all the working container
podman container ls
# Enter to the container
podman container exec -it {container id} ash
```

## Edit something
```yaml
cd /usr/share/nginx/html
vi index.html

# Do something in index.html

# Observe the change of the container
podman container diff {container name}

# Will See something as follows
# C -> Changed
# A -> Added
# D -> Deleted
C /etc
C /etc/nginx/conf.d
C /etc/nginx/conf.d/default.conf
C /root
A /root/.ash_history
A /run/nginx.pid
C /usr/share/nginx/html/index.html
C /var/cache/nginx
C /var
C /var/cache
A /var/cache/nginx/client_temp
A /var/cache/nginx/fastcgi_temp
A /var/cache/nginx/proxy_temp
A /var/cache/nginx/scgi_temp
A /var/cache/nginx/uwsgi_temp
```

## Commit and Build Image
```yaml
# Commit container to an image
podman commit {container name / id} {image name}

# Check whether a new image is created
podman images

# Run the new image
podman run -d -p 5566:80 {image name}

# Exception 
Error: cannot listen on the TCP port: listen tcp4 :5566: bind: address already in use
(Some container used this port)

# Solution
## Step 1. Find out which container is using that port at the moment
podman ps | grep 5566

## Step 2. Stop and Delete the old container
podman stop {old container ID / Name}
podman rm {old container ID / Name}

## Step 3. Activate the image again
podman run -d -p 5566:80 {image name}
```