# Amazon Simple Storage Service (S3)

## What is S3?
> Amazon Simple Storage Service (Amazon S3) is an object storage service that offers industry-leading scalability, data availability, security, and performance. This means customers of all sizes and industries can use it to store and protect any amount of data for a range of use cases, such as websites, mobile applications, backup and restore, archive, enterprise applications, IoT devices, and big data analytics. Amazon S3 provides easy-to-use management features so you can organize your data and configure finely-tuned access controls to meet your specific business, organizational, and compliance requirements. Amazon S3 is designed for 99.999999999% (11 9’s) of durability, and stores data for millions of applications for companies all around the world.
* MainPoints:
    1. An *object-based storage system*
    2. Access the object in the bucket via URL
        * We will store our **data/files (objects)** inside the **container (bucket)** with the **REST API request**
    3. The size limit of a single file is *0 bytes to 5 TB*, with no limit on overall storage capacity.
    4. After successfully upload a file to S3, you will receive HTTP 200 response.
    5. By default, a single AWS account can store up to 100 buckets. However, you can request AWS to increase the limit.

## Terminology
1. Durability
   * Protection against data loss, data corruption
   * S3 offers 99.99999999999 (11 9s) durability 
   * It means that the data is always safe against loss.
2. Availability
   * A measurement of the amount of time the data is available to you
   * expressed as a percent of time per year, E.G: 99.99%

## Object
* The file that you want to upload / store inside the bucket
* The data consists of following items:
  1. **Key**: object name
  2. **Value**: Actual data of the object / file
  3. **Version ID**: Version control with ID
  4. **Metadata**: Additional data used to record information related to the object.
    * Time of file upload
    * Time of last modification
  5. **Subresources**
    * Access Control Lists
    * Torrent

## How to Access object in bucket?
* We access them via *URL* and *HTTP protocol* 
* URL: bucket name + the region + the key
  * key: name of the object / file
* HTTP protocol
  * GET: Download the object
  * PUT: Upload the object
* Connection to S3
  1. Connect using public addresses via internet gateway
  2. Connect using private addresses via S3 Gateway endpoint.

## Storage Class
* Ref: S3StorageClassesPerformance.png
* Storage class adjustments can be made at object level, not just the bucket level.
* Minimum capacity charge per object: Each object you store will be charged at a minimum of 128kB.

### S3 Standard  
* default storage class 

### IA (Infrequently Accessed)
* *Access frequency is lower* compared to the Standard Storage Class, but when needed, the *data can still be retrieved immediately*
* Cost is cheaper than Standard Storage Class, but there is a *minimum charge for 30 days of storage*
* Access Performance is slower than Standard Storage Class
* Usage: Disaster recovery, backup...

## One Zone - IA
* One Availability Zone
* The data will total lost when the availability zone is crashed
* Better access performance because the data is stored in a single Availability Zone 
  * Lower latency and higher throughput 
* Cheaper than IA 
* Usage: Second backup, temporary datasets...

### S3 Standard intelligent-tiering
* Automatically move infrequently accessed files to a most cost-effective access tier, while frequently accessed remain in the standard tier
  > IA tier at most, and will not automatically move it to a lower-cost tiers like One Zone IA or Glacier

### Glacier
* For *Archiving data* (~History Data)
* Data is automatically encrypted using AES-256 bit encryption when stored
* *minimum charge for 90 days of storage*

### Glacier Deep Archive
* Lowest cost storage
* *minimum charge for 180 days of storage*
* Usage: 
  1. For industries that retain datasets for 7-10 years to meet regulatory compliance requirements
  2. Backup
  3. Disaster recovery

## Ways to access to buckets in S3 
* We can access to buckets in S3 via *IAM Policies*, *Bucket Policies*, and *Access Control List (ACLs)* 
* IAM Policies and Bucket Policies are recommended to use rather than ACLs
### IAM Policies
* Identity-based policies (User, Group, Role -> Principal)
* We can specify what actions are allowed on what AWS resources with policies, and attach the policy to the user, user group, or role 
* Written in JSON using the AWS access policy language
* **To conclude, IAM Policy is used to define what actions a principal can perform in their AWS environment**
* From an audit perspective, if the goal is to answer questions like *"What can a specific user do in the AWS environment?"*, using IAM policies is appropriate.
* If you need to control access to AWS services other than S3, you may use IAM policies.
* If you have numerous S3 buckets each with different permission requirements, you may use IAM policies.

### S3 Bucket Policies
* Resource-based policies
* attached to Amazon S3 buckets only

### S3 Access Control List (ACLs)
* *Legacy access control mechanism* that predates IAM
* It can be attached to a bucket or object directly

## S3 Versioning
* Versioning is a means of keeping multiple variants of an object in the same bucket.
* Use it to preservce, retrieve, and restore every version of every object stored in your S3 bucket
* Recover objects from *accidental delection* or *overwrite* easily

## S3 Replication
* Cross-Region Replication (CRR)
  * Replicate objects in a source S3 bucket to a destination S3 bucket
  1. Reduce latency for users accessing objects in different geographic locations.
  2. Improve the operational efficiency of compute systems accessing objects in S3
* Same-Resion Replication (SRR)

## S3 Lifecycle Management
* Transition Actions: Define when objects transition to another storage class
* Expiration actions: Define when objects expire (deleted by S3)

## S3 Encryption
* All S3 buckets and objects have encryption configured by default
* No additional cost and no impact on performance when encryption is done
### Encryption options
1. Server side encryption with S3 manage keys (SSE-S3)
   * Default encryption method
2. Server side encryption with AWS KMS managed keys (SSE-KMS)
3. Server side encryption with Client provided keys (SSE-C)
4. Client-side encryption
   * The encryption and decryption is taking place on client side, not server side / in AWS.
   * AWS just see the encrypted objects and it has no way to decrypting them.
 
## File Storage VS Object Storage
### File Storage
* Store data in **directories**, create hierarchies of directories
* Network connection is maintained (once you mounted that file system, it's there for you to use and save data)
* E.G: Windows, Amazon EFS

### Object Storage
* Store data in bucket, flat namespace (no hierarchies of directories)
* hierarchies can be mimicked with prefixes
* Access by REST API and cannot be mounted
* Network connected is completed (close immediately) after each REST API request

## Reference
1. https://docs.aws.amazon.com/zh_tw/AmazonS3/latest/userguide/Welcome.html
2. Storage Class: https://aws.amazon.com/tw/s3/storage-classes/#General_purpose 