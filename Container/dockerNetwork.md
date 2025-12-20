# Docker Network
* Docker networking allows containers to communicate with each other and the outside world
* When creating containers, use `--network` flag to specify the network model
* Docker provides multiple network drivers for different use cases

## Network Drivers Overview

Docker offers several built-in network drivers:

1. **Bridge** (Default): Containers on same host communicate via private internal network
2. **Host**: Container shares host's network stack directly (Podman 不需要建立 network，和宿主機共用相同的網路模型即可)
3. **None**: Disables all networking for the container (不需要管理任何網路功能，只要建立一個隔離網路空間就可以)
4. **Overlay**: Enables communication between containers across multiple Docker hosts (Swarm)
5. **Macvlan**: Assigns MAC address to container, making it appear as physical device on network

## None
```yaml
# Example code
podman run --network=none -d --name networktest jonlabelle/network-tools

# Example Code (Activate the container with tools, will be deleted automatically after exit the container)
podman run --rm -it --network=none jonlabelle/network-tools ifconfig -a

# Result
lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
# Only loopback interface can be found, but not other network card
# Therefore, this container does not have connections
```
* 使用 Situation: Batch Processing & High Security Concerns 

## Bridge
```yaml

```

# Useful Commands
```yaml
# Show network related commands
podman network --help

# Create network
podman network create {network name}

# Show / List all network
podman network ls

# Delete network

```