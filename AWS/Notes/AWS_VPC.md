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
2. **Availability Zone (AZ) 邏輯資料中心**
   * Region has multiple AZs (at least 3)
   * We can create *public (public access) & private (internal usage, no direct connectivity from the outside world) subnet (~IP networking space)* inside the AZs
   * We can deploy *EC2 instances* into public / private subnet
   * *VPC router* will take care of routing within the VPC and the outside of the VPC
   * *Internet gateway* attaches to VPC and connect to the Internet
     * egrass internet: send data out of the outside Internet 
     * ingress internet: receive data from the outside Internet
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
* Red Border == Region (e.g )

* VPC Router takes care of all routing for connections that are going outside of a subnet (within the VPC and outside of VPC)
* Internet Gateway is connected to VPC router, for sending data out of the Internet (IPv4 network, inbound & outbound connection)
  * Egress-only Internet Gateway is for IPv6 network (Outbound connection only)
* Peering Connection: Direct connection between two VPCs
* VPC Endpoints: Private Connection to public AWS service
* NAT instance: Enable Internet access for EC2 instances in private subnets (managed by you) outbound only
* NAT Gateway: Enable Internet access for EC2 instances in private subnets (managed by AWS) outbound only
* Security Group: Instance-level firewall
* Network ACL: Subnet-level firewall (only sees traffic going in and out of the subnet)
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

### Network ACLs
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

## Reference
1. https://hackmd.io/@AWSlearning/BJvnmhRg2#%E2%97%86-NACL-vs-SG-%E7%9A%84%E5%AE%89%E5%85%A8%E8%A8%AD%E5%AE%9A%E4%BB%8B%E7%B4%B9 (AWS VPC 網路架構 (觀念講解篇))