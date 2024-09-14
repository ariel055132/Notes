# Amazon Simple Storage Service (S3)

## What is S3?
> Amazon Simple Storage Service (Amazon S3) is an object storage service that offers industry-leading scalability, data availability, security, and performance. This means customers of all sizes and industries can use it to store and protect any amount of data for a range of use cases, such as websites, mobile applications, backup and restore, archive, enterprise applications, IoT devices, and big data analytics. Amazon S3 provides easy-to-use management features so you can organize your data and configure finely-tuned access controls to meet your specific business, organizational, and compliance requirements. Amazon S3 is designed for 99.999999999% (11 9’s) of durability, and stores data for millions of applications for companies all around the world.
* MainPoints:
    1. An *object-based storage system*
    2. Access the object in the bucket via URL
        * We will store our **data/files (objects)** inside the **container (bucket)** with the **REST API request**

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
* All data will be stored to *S3 standard* automatically if you don't specify where you want to store the object.
* *S3 Standard intelligent-tiering* will automatically move data between storage classes based on how you are actually utilizing that data -> Cost and Performance Optimization
* Minimum capacity charge per object: Each object you store will be charged at a minimum of 128kB.
* *IA*: Infrequently accessed data
* *Glacier*: For Archival data (~History data)
### 

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