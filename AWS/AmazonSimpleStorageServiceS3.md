# Amazon Simple Storage Service (S3)

## What is S3?
> Amazon Simple Storage Service (Amazon S3) is an object storage service that offers industry-leading scalability, data availability, security, and performance. This means customers of all sizes and industries can use it to store and protect any amount of data for a range of use cases, such as websites, mobile applications, backup and restore, archive, enterprise applications, IoT devices, and big data analytics. Amazon S3 provides easy-to-use management features so you can organize your data and configure finely-tuned access controls to meet your specific business, organizational, and compliance requirements. Amazon S3 is designed for 99.999999999% (11 9’s) of durability, and stores data for millions of applications for companies all around the world.
* MainPoints:
    1. An *object-based storage system*
    2. Access the object in the bucket via URL
        * We will store our **data/files (objects)** inside the **container (bucket)** with the **REST API request**
    3. The size limit of a single file is *0 bytes to 5 TB*, with no limit on overall storage capacity.
    4. After successfully upload a file to S3, you will receive *HTTP 200 response*.
    5. By default, a single AWS account can store up to *100 buckets*. However, you can request AWS to increase the limit.
    6. S3 is a universal namespace so *bucket names must be unique globally*
        * Best practice to create buckets in regions that are physically closest to you users to reduce latency 

## Terminology
1. Durability
   * Protection against data loss, data corruption
   * S3 offers 99.99999999999 (11 9s) durability 
   * It means that the data is always safe against loss.
2. Availability
   * A measurement of the amount of time the data is available to you
   * expressed as a percent of time per year, E.G: 99.99%

## S3 Object
* The file that you want to upload / store inside the bucket
* Supports any file type
* Permission can be defined on objects at any time
* Storage class is set at the object level
* The data consists of following items:
  1. **Key**: object name, which is used to store and retrieved
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
* Better access performance as data is stored in a single Availability Zone 
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
* **Identity-based policies** (User, Group, Role -> Principal)
* We can specify what actions are allowed on what AWS resources with policies, and attach the policy to the user, user group, or role 
* Written in JSON using the AWS access policy language, where *principal* element is not required in the body
* **To conclude, IAM Policy is used to define what actions a principal can perform in their AWS environment**
* From an audit perspective, if the goal is to answer questions like *"What can a specific user do in the AWS environment?"*, using IAM policies is appropriate.
* If you need to control access to AWS services other than S3, you may use IAM policies.
* If you have numerous S3 buckets each with different permission requirements, you may use IAM policies.

### S3 Bucket Policies
* Resource-based policies
* attached to Amazon S3 buckets only
* Use it when you want to grant cross-account access to S3 environment, without using IAM roles
* Use it instead of IAM policies when your IAM policies are reaching the size limits.

```json
example of IAM policy
{
  "Version": "2012-10-07",
  "Statement": [
    {
      "Sid": "Statement1",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "bucket/*"
    }
  ]
}
```

### S3 Access Control List (ACLs)
* *Legacy access control mechanism* that predates IAM, not recommended
* It can be attached to a *bucket* or *object* directly

## S3 Versioning (版本控制)
* Versioning is a means of keeping multiple variants of an object in the same bucket.
* Use it to preservce, retrieve, and restore every version of every object stored in your S3 bucket
* Recover objects from *accidental delection* or *overwrite* easily
* Versioning is *disabled* in default
* Versioning can be enabled by 
  1. Bucket Owners (root account)
  2. AWS account that created the bucket
  3. Authorized IAM users

## S3 Replication
### On Demand Replication

### Live Replication
* Cross-Region Replication (CRR)
  * Replicate objects in a *source S3 bucket to a destination S3 bucket*
  1. Reduce latency for users accessing objects in different geographic locations.
  2. Improve the operational efficiency of compute systems accessing objects in S3
* Single-Region Replication (SRR)
  * Replicate objects across S3 bucket in the same AWS region

## S3 Lifecycle Management
* In order to manage the objects so that they are *stored cost effectively* throughout their lifecycle, we need *Lifecycle Management configuration*
## Transition Actions 轉換動作
* Define when *objects transition to another storage class*
* Rules Ref: S3TransitionActions.jpg
* General Rule 與 Specific 其實就是 S3TransitionActions.jpg 的 Rule
### General Rule
1. Only objects with a *size of more than 128KB* can be transitioned.
2. *S3 Standard* storage class can be transited to any other storage class.
3. Any storage class to the *Glacier* or *Deep Archive* storage class.
### Specific Rule
4. *S3 Standard-IA* storage class can be transited to *S3 Intelligent-Tiering* or *S3 One Zone-IA* storage class.
5. *S3 Intelligent-Tiering* storage class can be transited to *S3 One Zone-IA* storage class.
6. *S3 Glacier* storage class can be transited to *S3 Glacier Deep Archive* storage.

## Expiration Actions
* Define when objects expire (deleted by S3)

## S3 Encryption
* All S3 buckets and objects have encryption configured by default
* No additional cost and no impact on performance when encryption is done
### Encryption options
1. Server side encryption with S3 manage keys **(SSE-S3)**
   * Default encryption method
2. Server side encryption with AWS KMS managed keys **(SSE-KMS)**
   * Use a key generated and managed by AWS KMS
3. Server side encryption with Client provided keys **(SSE-C)**
   * Upload you own AES-256 encryption key which S3 uses when it writes object
4. Client-side encryption
   * The encryption and decryption is taking place on client side, not server side / in AWS.
   * AWS just see the encrypted objects and it has no way to decrypting them.

## Multipart upload & Transfer Acceleration
* Upload approaches
### Multipart upload
* Upload objects in parts independently, in parallel and in any order
* ~Split the files into multiple parts, and upload them in parallel
* can be used for objects from 5 MB up to 5 TB
* Must be used for objects larger than 5GB
### Transfer Acceleration
* enabled at the bucket level
* Uses CloudFront edge locations to improve performance of transfers from client to s3 bucket
* tries to get content closer to users by caching it in edge locations around the world 
* AWS only charges if there is a performance improvement
* Useful when a company is looking to *improve the speed of uploading from a very remote location somewhere far away from the bucket*.
* Need to enable transfer acceleration on the S3 Bucket, and it cannot be disabled, but suspended only

## S3 Select and Glacier Select
* S3 Select: Use *SQL expressions* to access the individual object rather than the whole object.
* Glacier Select: Same as the above but from the archive database.

## Server Access Logging
* *log* around the events/requests that happen in Amazon S3 buckets
* Details include *the requester, bucket name, request time, request action, response status, and error code*
* Disabled by default, need to setup 
* Only pay for the storage space used
* must configure a separate bucket as the destination
* grant write permissions to the Amazon S3 Log Delivery group on destination bucket

## Cross-Origin Resource Sharing (CORS)
* Origin: Defined by DNS name, protocol, and port
  * For example, you are connect from a client to a specific domain name using HTTP (protocol) on port 80
* Allows requests from an origin to another origin

## S3 Object Lamdba
* use Lamdba functions (self-defined / pre-built) to process the output of S3 GET requests
1. PII Access Control - detect PII and restricts access
2. PII Redaction - detect PII and return documents with the PII redacted
3. Decompression - decrypts objects compressed with bzip2, etc.

## File Storage VS Object Storage
### File Storage
* Store data in **directories**, create hierarchies of directories
* Network connection is maintained (once you mounted that file system, it's there for you to use and save data)
* E.G: Windows, Amazon EFS (C:\Users\ZZ01XXXXX\Documents...)

### Object Storage
* Store data in bucket, **flat namespace** (no hierarchies of directories)
* hierarchies can be mimicked with prefixes
* Access by REST API and cannot be mounted
* Network connected is completed (close immediately) after each REST API request

## S3 Multi-Factor Authentication Delete (MFA Delete)
* Adds MFA requirement for bucket owners to the following operations
  1. Changing the versioning state of the bucket
  2. Permanently deleting an object version
* The **x-amz-mfa** request header must be included in the requests
* Second Factor: Token generated by a hardware device or software program
* Version need to enable before implementing MFA

## S3 Performance Optimization
1. S3 support at least 3500 PUT/COPY/POST/DELETE or 5500 GET/HEAD requests per second per prefix in a bucket
2. increasing read or write performance by parallelizing reads (~multipart upload)
3. Use Byte-Range Fetches
4. Retry Requests for Latency-Sensitive Applications
5. Combine Amazon S3 (Storage) and Amazon EC2 (Compute) in the same AWS Region
6. Use Amazon S3 Transfer Acceleration to mimimize Latency caused by distance

## Architecture Patterns - Amazon S3
1. If company is concerned about **accidental deletion** of Amazon S3 objects
   * Enable *S3 Versioning* (recover objects easily)
2. Data stored in S3 is frequently accessed for 30 days then is rarely accessed, but must be immediately retrievable
   * Use a *lifecycle policy* to transition objects from *S3 standard to S3 Standard-IA* after 30 days.
   * Objects is saved to S3 standard bucket in default
   * rarely accessed, but immediately retrievable -> IA, but not Glacier (not immediately retrievable)
3. A backup of S3 objects within a specific folder in a bucket must be **replicated to another region**
   * Configure *cross-region replication* and specify the folder name as a prefix
   * **Q. Why need to specify the folder name as a prefix.**
4. Previous versions of objects in a versioning-enabled S3 bucket must be stored long term at the **lowest cost**
   * Create a lifecycle policy/rule that transitions previous versions to S3 Glacier Deep Archive.
   * Stored at lowest cost: S3 Glacier Deep Archive
5. A company wishes to manage all encryption of S3 objects through their application with **their own encryption keys**
   * Use *client-side encryption* with client managed keys
   * Their own encryption keys

## Reference
1. https://docs.aws.amazon.com/zh_tw/AmazonS3/latest/userguide/Welcome.html
2. Storage Class: https://aws.amazon.com/tw/s3/storage-classes/#General_purpose 
3. S3 Replication: https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html