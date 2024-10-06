# AWS DNS, Caching, and Performance Optimization
* **Amazon Route 53**: DNS Server
* **Amazon CloudFront**: Content delivery network
* **AWS Global Accelerator**: similar as Amazon CloudFront

   
## Amazon Route 53
* An advanced DNS (with more routing policy)
* You can transfer domains to Route 53 only if the Top-Level Domain (TLD) is supported
* You can transfer a domain from Route 53 to another registrar by contacting AWS support
* You can transfer a domain to another account in AWS
* You can have a domain registrated in one AWS account and hosted zone in another AWS account

### Amazon Route 53 - Hosted Zone
* Container for records, which include information about how to route traffic for a domain (such as example.com) and all of its subdomains (such as www.example.com, retail.example.com)
* **Just finding the domain name**, but not its IPs
1. *Public Host Zone*
   * determines how traffic is routed on the **Internet**
   * It can be query if other are using the correct DNS server setting
2. Private Hosted zone for VPC
   * determines how traffic is routed within **VPC**
   * Need to set enableDnsHostname, enableDnsSupport to true

## Amazon CloudFront Origins
* Ref: AmazonCloudFront_Concept_V2.png
1. CloudFront is a *CDN service* provided by AWS through *edge servers deployed worldwide*. (AWS 透過建立在全世界各地的 edge server所提供的CDN服務)
  * CDN (Content Delivery/Distribution Network) 內容傳遞網路
    * A geographically distributed network of proxy servers and their data centers
    * Goal is to provide high availability and performance by distributing the service spatially relative to end users 
  * Why edge servers have to established around the world?
    * Ensure that most users have a relatively closer source to access data
2. *Origin*: The location where content is stored, and from which CloudFront gets content to serve to viewers
3. *Edge Location*: A place to place edge servers 
   * users can obtain data and input data to edge location
   * it will cache the data from 
   * Currently has 210 edge locations
4. *Distribution*: Endpoints provided by CDN service, allow users to access the nearest edge server
  * name / access point of distribution & Multiple source of origin inside distribution
  * define behaviors (Path Pattern, Viewer Protocol Policy, Cache Policy, Origin Request Policy)
  * Currently **support web distrbition** only
    1. Speed up distrbution of static and dynamic content
    2. Distribute media files using HTTP and HTTPS
    3. Add, update, or delete object, and submit data from web forms
  * RTMP (~live streaming) is not supported since 2020

## Advantages of using CloudFront
1. Users can fetch data from the nearest edge server, resulting in much **faster access** speed and significantly improve user experience (使用者可以從最近的 edge server 拉資料，速度快多了，體驗自然大幅上升)
2. **Cost is lowered**, because the amount of data transmitted

## CloudFront Caching
* Ref: AmazonCloudFront_CachingBasic.png
* Objects are cached for a Time To Live (TTL) period, which defaults to 24 hours.
* Decreasing the TTL is beneficial for Dynamic Content as it ensures that the content is updated more frequently.
* Increasing TTL is better for performance and reduces load on the origin
* The transfer of the objects is through AWS Global Network, which ensures low latency, consistency, high throughput, and performance
### Basic Procedure
* Assume a user wants to find the object in edge location
1. User performs HTTP GET
2. Edge location receives the GET request. It tries to find the object that the user wants is inside the edge location or not.
   * If Yes, return the object to user from edge location. End
   * If the version of an object is stale (TTL expired) or the object is deleted by the user, it will send a request to the regional edge cache to fetch the object, and return the object to the user afterwards.
   * Version of an object is stale (TTL expire) / the object is deleted by user
3. Regional Edge Cache receive the request from edge location. It tries to seek for the object
   * If found, return the object to edge location.
   * If not (cache miss), it will send a request to the origin to fetch the object, and send it to the edge location afterwards.

## Path Patterns
* Ref: AmazonCloudFront_PathPattern.png
* Objective: Allow administrators to route traffic to different Origins based on the request content

## CloudFront SSL/TLS (Server Name Indication)
* Get the certificate from AWS Certificate Manager from us-east-1 or trusted third party CA
* Default CF Domain name can be changed using CNAMES
1. S3 Origins has its own certificate (cannot be changed)
2. You can put your own certificates or use ACM to generate certificate to Custom Origin.


## Lamdba@Edge
* Allows you to run Node.js and Python functions to *customize the content CloudFront delivers*

## AWS Global Accelerator
* A network service allows you to utilize the AWS Global Network to send data to your applications
* Get better bandwidth and latency and much more consistency

### Notes
1. Headers can be used to control the cache
   * *Cache-Control max-age=(seconds)* : Specifies how long CloudFront should wait before fetching the object again from the origin server
   * *Expires* : Specify an expiration date and time

## Architecture Patterns
1. An elastic Load Balancer must be resolvable using a company's public domain name. A route 53 hosted zone exists.
   * Create an **Alias** record that records the domain name to the ELB.
2. A website runs across *two AWS regions*. All traffic goes to one region and *should be redirected only if the website is unavailable*.
   * Create a **failover routing policy** in AWS Route 53 and configure health checks on the primary
3. Websites run in several countries and distribution rights require *restricting access to content based on the geographic source of the distribution*.
   * Use AWS Route 53 **geolocation routing policy** and restrict distributions based on geographic location.
4. A CloudFront distribution has multiple S3 Origins. Requests should be served from different origins based on file type being requested. **(Question)**
   * Modify the CloudFront behavior and configure a path pattern.
5. Content is accessed using an application and CloudFront distribution. Need to control access to multiple files on the distribution **(Question)**
   * Configure signed cookies and update the application
6. Application runs behind an Application Load Balancer in multiple Regions. Need to intelligently route traffic based on latency and availability.
   * Create an AWS Global Accelerator and add the ALBs.

## Reference
1. http://dns-learning.twnic.net.tw/bind/intro6.html (DNS Introduction)