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
   * We can create public (public access) & private (internal usage) subnet inside the AZs
3. **Data Center 實體資料中心**
   * The actual place where servers and hardware equipment are installed (實際放上主機與硬體設備等的地方)
   * An availability zone is composed of one or more data centers
4. **AWS global network**
   * Regions are connected to AWS global network
   * managed the network latency, performance....
   * Ensure the data transfer is fast
* You can spread your data, instances to several AZs (High Availability), less correlation in terms of failure.
* **AWS Outposts** (內部部署私有雲端): On-premises servers can deploy their subnet/instance inside, and connect to region
* **AWS Local Zone**: ~AZ, but resources is deployed a bit closer to where you are (lower latency when you access the resources)
* **AWS WaveLength Zone**: For make instance available to 5G network

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

## Reference
1. https://hackmd.io/@AWSlearning/BJvnmhRg2#%E2%97%86-NACL-vs-SG-%E7%9A%84%E5%AE%89%E5%85%A8%E8%A8%AD%E5%AE%9A%E4%BB%8B%E7%B4%B9 (AWS VPC 網路架構 (觀念講解篇))