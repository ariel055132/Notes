# Docker Network
* Docker networking allows containers to communicate with each other and the outside world
* When creating containers, use `--network` flag to specify the network model
* Docker provides multiple network drivers for different use cases

## Network Drivers Overview

Docker offers several built-in network drivers:

1. **Bridge** (Default): Containers on same host communicate via private internal network
2. **Host**: Container shares host's network stack directly
3. **None**: Disables all networking for the container (不需要管理任何網路功能，只要建立一個隔離網路空間就可以)
4. **Overlay**: Enables communication between containers across multiple Docker hosts (Swarm)
5. **Macvlan**: Assigns MAC address to container, making it appear as physical device on network

## None