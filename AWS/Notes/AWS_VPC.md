# Amazon VPC (Virtual Private Cloud)
* Logically isolated portion of the AWS Cloud in which you can deploy your own AWS resources in a kind of private space
* Complete control over virtual networking environment include:
  1. Including section of own IP address range
  2. Creation of subnets (public and private subnets)
  3. Configuration of route tables and network gateways

## AWS Global Infrastructure
* Ref: AWSGlobalInfrastructure.png
1. **Region 區域**
   * Separate physical separation in the world (一個實體地區，例如：東京，德州...)
   * Each region consists of multiple Availability Zone
2. **Availability Zone (AZ) 邏輯資料中心**
   * Region has multiple AZs (at least 3)
   * We can create subnet inside the AZs:
      * *public subnet*: Has a direct route to internet gateway, Resources in a public subnet can access the public Internet  
      * *private subnet*: Does not have a direct route to internet gateway, require a *NAT* device to access the public internet
   * We can deploy *EC2 instances* into public / private subnet
   * *VPC router* will take care of routing within the VPC and the outside of the VPC
   * *Internet gateway* attaches to VPC and connect to the Internet
     * *egrass internet*: send data out of the outside Internet 
     * *ingress internet*: receive data from the outside Internet
3. **Data Center 實體資料中心**
   * The actual place where servers and hardware equipment are installed (實際放上主機與硬體設備等的地方)
   * An availability zone is composed of one or more data centers
4. **AWS global network**
   * Regions are connected to AWS global network
   * managed the network latency, performance....
   * Ensure the data transfer is fast
* Advantages: 
  * *High Availability*: You can spread your data, instances to several AZs
  * *Less correlation* in terms of failure
* **AWS Outposts** (內部部署私有雲端): On-premises servers (aka. *Corporate data center*) can deploy their subnet/instance inside, and connect to region
* **AWS Local Zone**: ~AZ, but resources is deployed a bit closer to where you are, leads to lower latency
* **AWS WaveLength Zone**: For make instance available to 5G network, for server and mobile applications
* **Amazon CloudFront Network**: Content Delivery Network, cache the content around the world, users access the content from the instances geographically near to them. E.G. Australia users will get the content from the instances in Australia, but not the US. 

## IP addressing 
### Structure of IPv4 Address
* Includes a **network and host ID**, defined by **subnet mask**
* IP addresses are written in **dotted decimal notation** (十進制)
* Each part of the address is a **binary octet** (二進制)
* E.G: 192.168.0.1
* 192 --> 11000000 = (2^7 + 2^6 = 128 + 64 = 192)
* 168 --> 10101000 = (2^7 + 2^5 + 2^3 = 128 + 32 + 8 = 168)
* 0 --> 00000000 = 0
* 1 --> 00000001 = (2^0 = 1)

### Networks and Hosts
* 192.168.0 --> network ID
* 1 --> Host ID (unique value per individual computer)

## VPC structure
* Ref: VPCStructure.png
### General
1. *Subnet*
   * segment of VPC's IP address range where user can place group of isolated resources 
2. *Internet Gateway* 
   * VPC side of a connection to the public internet (VPC 與外界 Internet 連線的方式)
   * Egress-only Internet Gateway is for IPv6 network (Outbound connection only)
3. *NAT (Network Address Translation) Gateway*
   * Services for resources in private subnet to access the Internet
   * (讓在Private Subnet的資源可存取外界 Internet，同時外界 Internet 無法與 Private Subnet 連線)
4. *Router* 
  * Interconnect subnets and direct traffic between Internet Gateways, virtual private Gateways, 
  * (透過 Router 連結 所有 Gateway，做 Routing)
5. *Peering Connection (VPC Peering)*
  * Direct connection between two VPCs
  * enables user to route traffic via private IP address between two peered VPCs
6. 
7. 

8. *VPC Endpoints*
  * Private Connection to public AWS service
9.  NAT instance
  * Enable Internet access for EC2 instances in private subnets (managed by you) outbound only
10. *Network ACL (Access Control List)*
  * Instance-level firewall
11. *Security Group* 
  * Subnet-level firewall (only sees traffic going in and out of the subnet)
* When you create a VPC, you must specify a range of IPv4 addresses for the VPC in the form of CIDR (Classless Inter-Domain Routing) blocks 

## AWS CIDR Blocks
* CIDR Block Size can be between /16 and /28
* Cannot overlap with any existing CIDR Blocks that is associated with the VPC
* Cannot increase / decrease the size of an existing CIDR block

## Security Groups and Network ACLs
* Protect EC2 instances, databases, and other services that sit inside an Amazon VPC
### Stateful and Stateless Firewall
* Stateful firewall allows the return traffic automatically
* Stateless firewall checks for an allow rule for both connections

### Network ACLs (Access Control List)
* Apply at the subnet level (Region -> Availability Zone -> Subnet)
* Check the ingress, engress network traffic to the subnet
* Do not check the traffic between instances (Subnet level)
* Support allow and deny rules
* Stateless
* Process rules in order
* Automatically applies to all instances in the subnets its associated with

### Security Group 
* Instance Level (Region -> Availability Zone -> Subnet -> Instances)
* Support allow rules
* Stateful
* Evaluates all rules
* Applies to an instance only if associated with a group

## VPC Peering
* Routing Addresses internally for VPCs

## VPC Endpoint
* https://joehuang-36936.medium.com/vpc-endpoints-interface-gateway-%E6%AF%94%E8%BC%83-5c9cf0f53723
* Connect to an instance in Amazon service without using the public internet (connect privately)
1. Interface Endpoint
2. Gateway Endpoint
   * Route table entry is required with the prefix list for destination and the gateway ID
* Service Provider Model

## AWS Client VPN
* Connect client computer to AWS data center / 

## Site to Site VPN
* Connects directly from AWS resources to Customer on-premises servers
* Virtual Private Gateway (VGW) - Customer Gateway

## AWS Direct Connect (DX)
* Ref: *source/VPC/AWS_Direct_Connect_DX.png* (General)
* Ref: *source/VPC/AWS_Direct_Connect_DX_2.png* (Private VIF & Public VIF)
* Private Connection into AWS
* DX Connections are not encrypted
* AWS Direct Connect Location
  * A DX port (1000-Base-LX or 10GBASE-LR) must be allocated in a DX location
  1. AWS Cage: AWS Direct Connect Endpoint
  2. Customer / Partner Cage: Customer / Partner router
* Advantages
  1. **Private connectivity** between AWS and on-premises data center / office
  2. **Consistent network experience** - increased speed/latency & bandwidth/throughput
  3. Lower costs for organizations that transfer large volumes of data
* Private VIF
  * Connect to a single VPC in the same AWS Region using a VGW
* Public VIF
  * Connect to AWS Public Services in any Region
  * Cannot connect to the Internet

## AWS Direct Connect Gateway

## AWS Transit Gateway
* Network transit hub that interconnects VPCs and on-premises networks

## Reference
1. https://hackmd.io/@AWSlearning/BJvnmhRg2#%E2%97%86-NACL-vs-SG-%E7%9A%84%E5%AE%89%E5%85%A8%E8%A8%AD%E5%AE%9A%E4%BB%8B%E7%B4%B9 (AWS VPC 網路架構 (觀念講解篇))
2. https://joehuang-36936.medium.com/vpc-endpoints-interface-gateway-%E6%AF%94%E8%BC%83-5c9cf0f53723 (VPC Interface Endpoints vs VPC Gateway Endpoints)