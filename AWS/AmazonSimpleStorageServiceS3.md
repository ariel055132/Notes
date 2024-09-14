# Amazon Simple Storage Service (S3)

## What is S3?
* An *object-based storage system*
* Access the object in the bucket via URL


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

## Terminlogy
1. Bucket
   * A container stores your objects.

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