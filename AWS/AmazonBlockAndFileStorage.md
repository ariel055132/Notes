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