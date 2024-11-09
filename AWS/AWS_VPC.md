# Amazon VPC (Virtual Private Cloud)
* Logically isolated portion of the AWS Cloud in which you can deploy your own AWS resources in a kind of private space
* Complete control over virtual networking environment include:
  1. Including section of own IP address range
  2. Creation of subnets (public and private subnets)
  3. Configuration of route tables and network gateways

## AWS Global Infrastructure
1. **Region 區域**
   * Separate physical separation in the world (一個實體地區，例如：東京，德州...)
2. **Availability Zone (AZ) 邏輯資料中心**
   * Region has multiple AZs (at least 3)
   * We can create subnet inside the AZs
3. **Data Center 實體資料中心**
   * The actual place where servers and hardware equipment are installed (實際放上主機與硬體設備等的地方)
   * An availability zone is composed of one or more data centers
4. **AWS global network**
   * Regions are connected to AWS global network
   * managed the network latency, performance....
   * Ensure the data transfer is fast
* You can spread your data, instances to several AZs (High Availability), less correlation in terms of failure.
* All of the regions are connected around the world by **AWS global network**, .


## Reference
1. https://hackmd.io/@AWSlearning/BJvnmhRg2#%E2%97%86-NACL-vs-SG-%E7%9A%84%E5%AE%89%E5%85%A8%E8%A8%AD%E5%AE%9A%E4%BB%8B%E7%B4%B9 (AWS VPC 網路架構 (觀念講解篇))