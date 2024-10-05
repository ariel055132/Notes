# Amazon Block And File Storage
* Object based storage: Amazon S3
* Block Storage: Amazon EBS (Elastic Block Store)
* File-based storage: Amazon EFS (Elastic File System)
* Multiple file system: Amazon FSx
* Gateway: AWS Storage Gateway

## Block vs File vs Object Storage
### Block Storage
* leads to **Hard drives** (HDD: Magnetic Drives; SSD: Flash Memory) 
* A lot of them use in cloud, as they are cost-effective and good for some cases
* The OS read/write at the **block level**. Disks can be internal, or network attached

### File Storage 
* A block based Storage that a **file system has been created on top**
* The file system can be shared by many users, and come from many sources

### Object Storage
* The user implements object operation to **bucket** with HTTP protocol, cannot be mounted
* Object can be all file type
* no hierarchy for files

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
* 