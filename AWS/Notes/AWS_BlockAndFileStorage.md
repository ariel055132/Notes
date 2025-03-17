# Amazon Block And File Storage

## Storage System
* There are multiple storage system in AWS
1. Block Storage -> Amazon Elastic Block Store (EBS)
2. File Storage -> Amazon Elastic File System (EFS)
3. Object Storage -> Amazon Simple Storage Services (S3)
4. Multiple file system: Amazon FSx
5. Gateway: AWS Storage Gateway

### Block Storage
* leads to **Hard drives** (HDD: Magnetic Drives; SSD: Flash Memory) 
* A lot of them use in cloud, as they are **cost-effective** and good for some cases
* The OS read/write at the **block level**, see volumes that can be partitioned and formatted 
* Disks can be internal, or network attached
* Ref: source/BlockAndFileStorage/BlockStorage.png

### File Storage 
* A block based Storage that a **file system has been created on top**
* The file system can be **shared by many users**, and come from many sources
* Disks always be network attached (E.G: NAS)
* Ref: source/BlockAndFileStorage/FileStorage.png

### Object Storage
* The user implements object operation to **bucket** (aka. Object Storage Container) with **HTTP protocol** (e.g GET, PUT, POST, SELECT, DELETE), cannot be mounted
* Object can be all file type (files, image, videos, doc, etc.)
* no hierarchy for files (no file path.)
* Ref: source/BlockAndFileStorage/ObjectStorage.png

## EBS Deployment and Volume Types
* Objectives
  * How to deploy our volumnes and connect to them
  * Understand the available volume types

### EBS Deployment
* EBS volume exists within a **single availability zone** only. 
* EBS volume data persists independently of the life of the instance
* EBS volume do not need to be attached to an instance
* The data is actually replicated to multiple copies in the same AZ. 
* Only one instances can be connected to one EBS volumn (Instance and EBS volume must in the same Availability Zone), multiple instances connect is forbidden (unless enable **EBS multiple attach**).
* You can *attached multiple EBS volumes to an instance* (E.G: 一個電腦可以有多個硬碟儲存資料~)
* Connect across availability zones is forbidden. (**Your instance must be in the same AZ as your volume**)
  * If you want to connect to another instances in different availability zone, you can create a **snapshot** of the volume, and put it to the new AZs.
* **Root EBS volumes are deleted** on termination by default. (When you terminate your instance, all of that data, that volume, will be completely deleted and lost forever)
* **Extra non-boot volumes are not deleted** on termination by default.
* Ref: source/BlockAndFileStorage/EBSDeployment.png

### EBS Multiple attach
* Connect from multiple instances to a single EBS volume, but it is only available for **Nitro system-based** EC2 instances.
* Up to **16 instances** can be attached to a single volume
* Must be a **Provisioned IOPS** io1 volume
* Must be **within a single AZ**
* Ref: source/BlockAndFileStorage/EBSMultiAttach.png

### EBS SSD-Backed Volumes
1. General Purpose SSD (gp2, gp3)
   * Default Type: gp3 
   * No EBS-multi attached supported
   * Usage: Low-latency interactive apps, development and test environments
2. Provisioned IOPS SSD (io2 block express, io2, io1)
   * io2 block express: 4TB-64Tb volume size
   * io2 & io1: 4GB-16TB volume size 
   * EBS-multi attached supported
   * Usage: Workload that require sub-mullisecond latency, sustained IOPS, I/O-intensive database workloads
* Ref: source/BlockAndFileStorage/SSDBackedVolumes.png

### EBS HDD-Backed Volumes
* Not support EBS-Multi Attach & Boot Volume
1. Throughput Optimized HDD
   * Use Case: Big Data, Data Warehouses, Log processing
2. Cold HDD
   * Use Case: Storage for data that is infrequently used, scenarios where the lowest storage cost is important
* Ref: source/BlockAndFileStorage/HDDBackedVolumes.png

### HDD-backed Volumes vs SSD-backed Volumes
* Storage，存 Log -> HDD-backed
* 日常運作 -> SSD-backed

## EBS Copying, Sharing, and Encryption
* We can backup data by creating **snapshot**
* Snapshot: 
  * A point in time copy of the data on the volume. 
  * Each snapshot is *incremental*.
  * For Example, user created three snapshots A (the earliest), B, C (the latest).
  * SnapShot A is the whole copy of the volume when it is created. SnapShot B is going to be the changes since Snapshot A. SnapShot C is going to be the changes since SnapShot B.
  * Therefore, SnapShot A + SnapShot B + SnapShot C === Volume
  * You can save up more spaces by deleting older snapshots and just keep the latest snapshots
* We can *create volume from a snapshot* in another AZ, then *creating an AMI* (Amazon Machine Image). And *attach the snapshot* to the image (~similar as copying the data to another)
* Ref: source/BlockAndFileStorage/EBSCopyingSnapShot.png

## EBS Snapshots and DLM (Data Lifecycle Manager)
* DLM (Data Lifecycle Manager): Automates the creation, retention, and deletion of EBS snapshots and EBS-backed AMIs
1. Protect valuable data by enforcing a *regular backup schedule*
2. Create standardized AMIs that can be refreshed at ergular intervals
3. Retain backups as required by auditors or internal compliance
4. Reduce storage costs by deleting outdated backups
5. Create disaster recovery backup policies that backup data to isolated accounts

## EC2 instance Volumes
1. Elastic Block Store Volumes (EBS)
   * Attached to *network*
   * Connect to them via ENI (Network Interface card)
   * data is persistent
2. Instance Store
   * *Physically* Attached to the host
   * Ephemeral - data is lost when the instance is powered down
   * high performance
   * temporary storage of information that changes frequently (buffers, caches, scratch data)
   * cannot be attaches / deattached

## Using RAID (Redundant Array of Independent Disks) with EBS
* *OS Level* (Not provided by AWS, configure through your OS)
* *RAID 0* and *RAID 1* are potential options on EBS
   1. RAID 0
      * striping data across disks 
      * Performance
      * If one disk fails, the entire RAID set fails
   2. RAID 1
      * Mirroring data across disks (Writing the same data to two different volumes)
      * Redundancy / Fault Tolerance
      * If one disk fails, the other disks is still working

## Amazon Elastic File System (EFS)
* Shared File System
* Connect instances to it from multiple availability zones (Regional)
* *Data Consistency*: Write operations for Regional File system are durably stored across Availability Zones
* *File Locking*: NFS Client applications can use NFS v4 file locking for read and write operations on EFS files
* Storage Class
  1. EFS Standard: Use SSDs for lower latency performance
  2. EFS Infrequent Access (IA): Cost effective option
  3. EFS Archive: Even cheaper for less active data (~Cold Storage)
* EFS Replication: data is replicated for disaster recovery purposes with RPO / RTO in the minutes
* Automatic Backup
* Performance Options
  * Provisioned Throughput: Specify a level of throughput that the file system can drive independent of the file system's size
  * Bursting Throughput: Scales with the amount of storage and supports bursting to higher levels

## Amazon FSx
* Fully managed *Third party file systems*
   1. Amazon FSx for Windows File Server: Windows-based application
   2. Amazon FSx for Lustre: Compute-intensive workloads (HPC)

### Amazon FSx for Windows File Server
* Native *Windows File System*
* Fully support for the SMB protocol, Windows NTFS, Microsoft Active Directory integration
   * Access Control Lists, shadow copies, user quotas
   * NTFS file system that can be accessed from up to thousands of compute instances using SMB protocol
* *High Availability*: replicates data within an Availability Zone
* *Multi-AZ*: file systems include an active and standby file server in separate AZs
* Ref: source/BlockAndFileStorage/AmazonFSxForWindows.png
   1. Multiple instances can connect to Amazon FSx for file storage.
   2. AWS Managed Microsoft AD is for authentication
   3. On-premises client can connect to FSx via VPN / Direct COnnect connection.

### Amazon FSx for Lustre
* Optmized for fast processing of workloads
* Works natively with *S3*, transparently access S3 objects as files, write the changes of files back to S3
* POSIX-compliant file system interface

## AWS Storage Gateway
* Connect on-premises storage to AWS
* Ref: source/BlockAndFileStorage/StorageGateway.png

### AWS Storage Gateway - File Gateway
* File Gateway
  * File System is mounted using NFS or SMB
  * A local cache provides low latency access to recently used data
  * A virtual gateway appliance runs on Hyper-V (Windows), VMWare (Linux), EC2 (AWS).
  * Files are stored in AWS

### AWS Storage Gateway - Volume Gateway
* Volume Gateway
   1. Cached Volume Mode
      * A cache of the most recently used data on-premise / on-site
      * Rest of the data is stored in S3
      * iSCSI: protocol for transfering data between gateway and server
   2. Stored Volume Mode
      * Entire dataset is stored on-site
      * Asynchronously backed up to S3 (snapshots)
   3. Tape Gateway
      * Backup server can use many common backup applications
      * S3 Standard is used for writing to tapes
      * Once tapes are ejected from backup / S3, stoed to S3 Glacier / S3 Glacier Deep Archive

## Architecture Patterns
1. Simple method for *backing up Amazon EBS Volumes* is required that is *fully automated*
   * Using DLM (Data Lifecycle Manager) to create a backup schedule
2. A distributed applications that has many nodes that each hold a copy of data that is synchronized between them. Need the best performance
   * Using Stored Volume Mode 
   * **This This This** Use instance stores for storing the data with the best performance
3. Application must startup quickly when launched by *Auto Scaling Group (ASG)* but *requires app dependencies and code to be installed*.
   * Create an AMI which contains application dependencies and code
   * Do not need to run the installation process of code when launching instances
4. Many Linux instances must be attached to a shared file system that scales elastically
   * **???**Create an Amazon EFS file system and mount from each instance.
5. Company requires a managed file system that uses the *NTFS file system*
   * Using Amazon FSx for Windows File Server
6. *On-premises servers* must be able to attach a block storage system *locally*. *Data should be backed up to S3 as snapshots*.
   * Using / Deploy an AWS Storage Gateway volume in stored volume mode.
7. An Amazon EBS volume must be *moved between Regions*.
   * Take a snapshots and copy the snapshot between Regions.
8. *Root EBS volumes* for a critical application *must not be deleted on termination*
   * Root EBS volumes must be deleted on termination, but extra non-boot volumes will not be deleted.
   * Therefore, we need to modify the delete on terminatino attribute when launching the EC2 instances.
9. On-permises servers use NFS to attach a file system. The file system should be replaced with an *AWS service that uses Amazon S3 with a local machine*.
   * Deploy an AWS Storage Gateway file Gateway.
