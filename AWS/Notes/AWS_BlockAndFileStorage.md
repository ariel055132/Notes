# Amazon Block And File Storage

## Storage System
* There are multiple storage system in AWS
1. Block Storage -> Amazon Elastic Block Store
2. File Storage -> Amazon Elastic File System
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

## EBS Copying, Sharing, and Encryption
* We can backup data by creating **snapshot**
* Snapshot: 
  * A point in time copy of the data on the volume. 
  * Each snapshot is *incremental*.
  * For Example, user created three snapshots A (the earliest), B, C (the latest).
  * SnapShot A is the whole copy of the volume when it is created. SnapShot B is going to be the changes since Snapshot A. SnapShot C is going to be the changes since SnapShot B.
  * Therefore, SnapShot A + SnapShot B + SnapShot C === Volume
  * You can save up more spaces by deleting older snapshots and just keep the latest snapshots
* We can create volume from a snapshot in another AZ, then creating an AMI (Amazon Machine Image). And attach the snapshot to the image (~similar as copying the data to another)
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
* Not provided by AWS, configure through your OS (*OS Level*)
* *RAID 0* and *RAID 1* are potential options on EBS
   1. RAID 0
      * striping data across disks 
      * Performance
      * If one disk fails, the entire RAID set fails
   2. RAID 1
      * Mirroring data across disks (Writing the same data to two different volumes)
      * Redundancy / Fault Tolerance
      * If one disk fails, the other disks is still working