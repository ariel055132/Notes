# Docker Network
* Docker networking allows containers to communicate with each other and the outside world
* When creating containers, use `--network` flag to specify the network model
* Docker provides multiple network drivers for different use cases

## Network Drivers Overview

Docker offers several built-in network drivers:

1. **Bridge** (Default): Containers on same host communicate via private internal network
2. **Host**: Container shares host's network stack directly (Podman 不需要建立 network，和宿主機共用相同的網路模型，代表著如果)
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

## Host
```yaml
podman run --rm -it --network=host jonlabelle/network-tools ifconfig -a

# Network config of the container
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 128.199.177.250  netmask 255.255.192.0  broadcast 128.199.191.255
        inet6 fe80::68e1:4dff:fefc:3c37  prefixlen 64  scopeid 0x20<link>
        ether 6a:e1:4d:fc:3c:37  txqueuelen 1000  (Ethernet)
        RX packets 446729  bytes 237974607 (226.9 MiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 354261  bytes 64577081 (61.5 MiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

eth1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 10.104.0.2  netmask 255.255.240.0  broadcast 10.104.15.255
        inet6 fe80::ec98:d5ff:fe56:d3ba  prefixlen 64  scopeid 0x20<link>
        ether ee:98:d5:56:d3:ba  txqueuelen 1000  (Ethernet)
        RX packets 65  bytes 4626 (4.5 KiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 382  bytes 18016 (17.5 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 1350  bytes 155767 (152.1 KiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 1350  bytes 155767 (152.1 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

podman0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 10.88.0.1  netmask 255.255.0.0  broadcast 10.88.255.255
        inet6 fe80::b40e:d3ff:fe12:1e38  prefixlen 64  scopeid 0x20<link>
        ether e2:ea:f5:75:51:c1  txqueuelen 1000  (Ethernet)
        RX packets 80  bytes 7244 (7.0 KiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 82  bytes 5859 (5.7 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

veth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::287a:d9ff:fe35:1908  prefixlen 64  scopeid 0x20<link>
        ether 7a:10:32:cf:a6:bf  txqueuelen 1000  (Ethernet)
        RX packets 80  bytes 8364 (8.1 KiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 122  bytes 8751 (8.5 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

# Observe the network config of host
ipconfig
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN mode DEFAULT group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP mode DEFAULT group default qlen 1000
    link/ether 6a:e1:4d:fc:3c:37 brd ff:ff:ff:ff:ff:ff
    altname enp0s3
    altname ens3
3: eth1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP mode DEFAULT group default qlen 1000
    link/ether ee:98:d5:56:d3:ba brd ff:ff:ff:ff:ff:ff
    altname enp0s4
    altname ens4
14: podman0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP mode DEFAULT group default qlen 1000
    link/ether e2:ea:f5:75:51:c1 brd ff:ff:ff:ff:ff:ff
15: veth0@if2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master podman0 state UP mode DEFAULT group default qlen 1000
    link/ether 7a:10:32:cf:a6:bf brd ff:ff:ff:ff:ff:ff link-netns netns-ff939ea1-3164-66c3-96ee-c19d771dfb20
```
* 透過上述指令的創造，可以發現該 container 內所看到的網卡資訊與外部主機的內容是完全一樣的，除了使用 ip link外，其他的指令如 ip addr, ifconfig, iptables-save, ipvsadm 等都會看到相同內容。
* network port 都會共用，因此如果外面已經有服務使用 port 80, 你就不能再跑一個 port 80 於相同的 address 上。

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