# Migration and Transfer
* Mostly is a company has on-premises servers / infra and how to migrate to AWS Cloud

## AWS Migration Tools Overview
1. AWS Application Discovery Service
   * Collect data about servers in on-permises Data Center (Agentless / Agent-based discovery)
   * Server hostnames, IP addresses, MAC addresses
   * As well as resource allocation and utilization details of key resources including CPU, network, memory, and disk
   * Data can be saved to S3 and queried with Athena / Quicksight
   * Data Center -> AWS Application Discovery Service -> S3
2. AWS Migration Hub 
   * Monitor migrations that use AWS / partner tools
3. AWS Application Migration Service
   * Automated, *incremental*, and *scheduled* migrations with servers, and those servers will be migrated to EC2 instances
   * The migration processed to CloudWatch Events and Lamdba for automate actions
   * Servers -> AWS Application Migration Service -> Launch Template -> EC2 instance
4. AWS Database Migration Service
   * Migrate Databases to RDS
   * Database -> AWS Database Migration Service -> Amazon RDS
5. AWS DataSync
   * Migrate the data from NAS / File Server, and into services like Amazon S3, Amazon FSX
   * NAS / File Server -> AWS DataSync -> Amazon S3 / EFS File System

## AWS Application Discovery Service
* Collect data from on-premises data center
1. Discovery Connector
   * Support VMWare server
   * Deploy per vCenter
   * Collect static Configuration Data, VM utilization metrics
   * Support OS running in VMware vCenter
2. Discovery Agent
   * Support VMware, physical server
   * Deploy per server
   * Collect static configuration data, time series performance info (export), network inbound/outbound (export), running processes (export)
   * Support OS including Amazon Linux, Ubuntu, Windows Server, CentOS

## AWS Server Migration Service (SMS)
* Agentless service for migrating on-premises and cloud-based VMs to AWS
* Source platforms can be VMware, Hyper-V or Azure
* AWS Server Migration Service Connector is installed on the source platform
* Server volumes are replicated (encrypted with TLS) and saved as AMIs which can then be launched as EC2 instances
* Can use application grouping and SMS will launched servers in a CloudFormation stack
* Replicate servers to AWS for 90 days 

## AWS Database Migration Service (DMS)
* Migrating databases from on-premises, Amazon EC2 / Amazon RDS
* Support homogenous migration (), as well as heterogeneous

## AWS Application Migration Service (MGN)
* Highly automated lift-and-shift (rehost) solution for migrating application to AWS
* Utilizes continuous, block-level replication and enables short cutover windows measured in *minutes*
* AWS recommend agent-based replication when possible as it support *continuous data protection (CDP)*
* However, agentless snapshot-based replication possible with the AWS MGN vCenter Client installed
* Server Migration Services (SMS) utilizes incremental, snapshot-based replication and enables cutover windows measured in *hours*

## Data Sync
* Secure, online service that automates and acclerates *moving data* between on premises and AWS Storage services
* Secure -> Data is encrypted in transit with *TLS*
* DataSync can copy data between
  * Network File System (NFS) shares
  * Hadoop Distributed File Systems (HDFS)
  * Self-managed object storage
  * AWS Snowcone
  * Amazon S3 buckets
  * Amazon Elastic File System (Amazon EFS) file systems
  * Amazon FSx (Windows, Lustre, OpenZFS, and NetApp ONTAP)

## AWS Snow Family
1. *AWS Snowball / Snowmobile* 
   * Migrating large volumes (50-80 TB, petabyte scale) of data to AWS physically
   * For situation that the company needs to move a large amount of data, but they only have a small Internet link
   * The company has a high-burdened Internet link, the existing Internet link will be affected when it is used to transfer the Internet 
2. *Snowball Edge Compute Optimized*
   * Provides block and object storage and optional GPU (100 TB, petabyte scale)
   * Use it for *Edge Cases* (Data Collection, machine learning and processing, and storage in environments with Intermittent connectivity)
   * For situation that have a factory somewhere and do not have good Internet link
3. *Snowball Edge Storage Optmized*
   * Provides block storage and Amazon *S3-compatible object storage* (100 TB, exabyte scale)
   * Use for local storage and large-scale data transfer
4. *Snowcone*
   * *Small device* use for edge computing, storage and data transfer
   * Can transfer data *offline* / online with AWS DataSync agent
* Differences between 2 and 3 = ="??

* *Snowball Client* is a software that is installed on a local computer and is used to identify, compress, encrypt and transfer data
* Use 256-bit encryption and tamper-resistant enclosures with TPM
* Optimization
  1. Use the latest Mac or Linux Snowball client
  2. Batch small files together
  3. Perform multiply copy operations at one time
  4. Copy from multiple workstations
  5. Transfer directories, not files
* Use cases
  1. Cloud data migration 
  2. Content distribution - send data to clients or customers
  3. Tactical Edge Computing - collect data and compute
  4. Machine Learning - run ML directly on the device
  5. Manufacturing - data collection and analysis in the factory
  6. Remote locations with simple data - preprocessing, tagging, compression

## 7 Rs of Migration Strategies
* The smaller number, the least effort, and so on.
1. Retire: No longer needed, get rid of it
2. Retain: Leave as is (revisit at a leter date)
3. Relocate: Move without modification (Lift & Shift)
   * Close the data center, unplugged the cables, rack the center up, and move it to another places, and switch on the center again
4. Rehost: OS/App moved to another host system (Lift & Shift)
   * The on-premises servers is move as EC2 instances
   * Recommened the *AWS Application Migration Service (MGN)*, AWS SMS and AWS VM Import / Export can also used
5. Repurchase: Use a different solution
   * Google drive -> Dropbox
6. Replatform: 
   * Database to RDS; server to Elastic Beanstalk
   * *AWS Database Migration Service (AWS DMS)* and Schema Conversion Tool (SCT) can be used for DB migration
   * *Custom AMI / code-level migration* can be used for Elastic Beanstalk migration
7. Refactor: Re-architect to a cloud-native serverless architecture
