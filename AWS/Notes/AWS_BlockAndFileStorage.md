# Amazon Block And File Storage
* Object based storage: Amazon S3
* Block Storage: Amazon EBS (Elastic Block Store)
* File-based storage: Amazon EFS (Elastic File System)
* Multiple file system: Amazon FSx
* Gateway: AWS Storage Gateway

## Storage System
* There are three storage system in AWS
1. Block Storage
2. File Storage
3. Object Storage

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

## EBS Copying, Sharing, and Encryption
* We can backup data by creating **snapshot**
* snapshot: A point in time copy of the data on the volume. Each snapshot is incremental. 
* We can create volume from a snapshot in another AZ, then creating an AMI (Amazon Machine Image). And attach the snapshot to the image (~similar as copying the data to another)

## EBS Snapshots and DLM
* DLM (Data Lifecycle Manager): Automates the creation, retention, and deletion of EBS snapshots and EBS-backed AMIs
1. Protect valuable data by enforcing a *regular backup schedule*
2. Create standardized AMIs that can be refreshed at ergular intervals
3. Retain backups as required by auditors or internal compliance
4. Reduce storage costs by deleting outdated backups
5. Create disaster recovery backup policies that backup data to isolated accounts