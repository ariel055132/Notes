# Amazon ELastic Compute Cloud EC2


## Objectives



## What is EC2?
* A service in which we can run EC2 instances (virtual servers come with different combinations of CPU, memory, storage, and networking)
* *AWS* manage EC2 host, while *EC2 host server* manage *EC2 instances*

## Public, Private, and Elastic IP address
### Public IP address
* Associated with a private IP address on the instance
* Lost when the instances is closed/stopped, another new public IP address is gained. (Dynamic address)
* Used in public subnets
* Free to use them.
* Cannot be moved between instances (because it will lose when you are trying to move the address.)

### Private IP address
* Retained when the instance is stopped
* Used in Public and Private Subnets

### Elastic IP address
* *static* public IP address.
* charged even you are not using
* Associated with a private IP address on the instance.
* Can be moved between instances and Elastic network adapters.

## EC2 Metadata
* Data about your EC2 instance
* Instance MetaData Service (IMDS) - V1: older and less secure
* Instance MetaData Service (IMDS) - V2: newer, more secure and requires a session token for authorization (default)

## EC2 User Data
* The code/script is run when the instance starts for the **first time**
* limited to **16KB** in raw form, before it is **base64-encoded**

## EC2 Placement Groups
* A way that you can control how AWS deploy your EC2 instances and place them within your availability zones or across availability zones. (控制EC2 instance在物理硬件上的放置方式)
1. **Cluster** 
   * Packs instances close together inside an Availability Zone.
   * This strategy enables workloads to achieve the *low-latency* network performance necessary for *tightly-coupled* node-to-node communication that is typical of high-performance computing *(HPC) applications*.
   * Disadvantages: When the hardware is failed, all the instances cannot be used.
2. **Partition**
   * Spreads your instances across logical partitions such that groups of instances in one partition *do not share the underlying hardware* with groups of instances in different partitions.
   * This strategy is typically used by *large distributed and replicated workloads*, such as Hadoop, Cassandra, and Kafka.
   * Each partition is located on a separate AWS rack.
   * Partitions can be in *multiple Availability Zone* (up to 7 per AZ)
3. **Spread**
   * Strictly places a small group of instances across *distinct underlying hardware* to reduce correlated failures.
   * Each instance is loacted on *a separate AWS rack*.

## Network Interfaces
1. ENI (Elastic Network Interface)
   * Basic adapter type for when you don't have any high-performance requirements
   * Can use with all instance types
2. ENA (Elastic Network Adapter)
   * Enhanced networking performance
   * Higher bandwidth and lower inter-instance latency
   * Must choose supported instance type
3. EFA (Elastic Fabric Adapter)
   * Use with high performance computing and MPI and ML use cases
   * Tightly coupled applications
   * Can use with all instance types


## Private Subnets and Bastion Hosts

## EC2 instance lifecycle
1. You get the Operating System of EC2 instances from AMI
2. Try to launch the EC2 instances (pending state)
3. After the EC2 instances is launched, it will change to running state
4. You can choose reboot, shut-down, stop the instances
   * Reboot: Rebooting state, then return to running state (== OS reboot, DNS name and all IPv4 and IPv6 addresses retained)
   * Shut-down: shutting-down state, then go to terminated state (== deleting the EC2 instances, cannot recover a terminated instance. Root EBS volumes are deleted)
   * Stop: Stopping state, relevant to EBS-backed volumes only, finally enter stopped state (instances is migrated to a different host, private IPv4 addresses and IPv6 addresses retained, public addresses released)


## NAT Gateways & Instances (Network Address Translations)
* Translate the address often between public address and private address
* Enable the instances that we deploy into private subnets to connect to the internet, but the internet outside cannot access to the private subnets instances
1. Deploy a NAT Gateway in a public subnet, the ec2 instances in private subnet connect to the NAT Gateway. (The NAT Gateway need to have a public IP address for communication --> elastic IP address)
* Before having NAT Gateway, NAT instances are created to do the same thing
  * Uses a special AMI with the string amzn-ami-vpn-nat 
  * Disable source/destination checks
* NAT instances vs NAT Gateway

## AWS Nitro System
* next generation of EC2 instances, support more virtualized and bare metal instances types
* Nitro instances and nitro enclaves
* Breaks the function in EC2 instances, put those function into specialized hardware with a Nirto Hypervisor --> Optimization, Security (hardware), Better performance (network, computing)

## Nitro Enclaves
* Isolated compute environments
* Runds on isolated and hardened virtual machines
* Protect and securely processes highly senitive data

## Reference
1. https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html
2. https://hackmd.io/@gdw7l5sPTOyNv76kZ_twjA/SJvjP7du3