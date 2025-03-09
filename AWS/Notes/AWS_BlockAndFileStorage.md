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

### File Storage 
* A block based Storage that a **file system has been created on top**
* The file system can be **shared by many users**, and come from many sources
* Disks always be network attached (E.G: NAS)

### Object Storage
* The user implements object operation to **bucket** (aka. Object Storage Container) with **HTTP protocol** (e.g GET, PUT, POST, SELECT, DELETE), cannot be mounted
* Object can be all file type (files, image, videos, doc, etc.)
* no hierarchy for files (no file path.)

## EBS Deployment and Volume Types
* Objectives: How to deploy our volumnes and connect to them, Understand the available volume types
* EBS volume exists within a **single availability zone** only. Although the data is actually replicated to multiple copies in the same AZ. 
* Only one instances can be connected to one EBS volumn, multiple instances connect is forbidden (unless enable EBS multiple attach).
* Connect across availability zones is forbidden. (**Your instance must be in the same AZ as your volume**)
* **Root EBS volumes are deleted** on termination by default. (When you terminate your instance, all of that data, that volume, will be completely deleted and lost forever)
* **Extra non-boot volumes are not deleted** on termination by default.

### EBS Multiple attach
* Connect from multiple instances to a single EBS volume, but it is only available for **Nitro system-based** EC2 instances.
* Up to **16 instances** can be attached to a single volume
* Must be a **Provisioned IOPS** io1 volume
* Must be **within a single AZ**

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