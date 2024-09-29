# AWS DNS, Caching, and Performance Optimization
* Introduction of the following setting
* Amazon Route 53: DNS Server
* Amazon CloudFront: Content delivery network
* AWS Global Accelerator: similar as Amazon CloudFront

## DNS (Domain Name System)
* Ref: *DNS_Procedure.png*
* Objective
  * Converting a website entered by the user into the IP address of the web server they wish to connect to
  * Input: domain name / website address (e.g www.google.com)
  * Output: IP address of the domain name (to be precise, host server IP)
* How it work (Procedure)
  1. Users enters website address (aka. Domain Names) in browser, for example: www.google.com
  2. DNS Server receive the domain names entered by user, it needs to resolved it to the IP address of the web server that the user wants to connect to
    * Each DNS server has a *zone file*, it contains lots of records that map the host name or the domain name to a value including IP addresses
    * DNS server is trying to map the domain name to the IP address, and return the IP to the user.
  3. Computer connects to the IP addresses given by DNS Server
   
## Amazon Route 53
* An advanced DNS (with more routing policy)
### Routing Policy
1. Simple
   * Ref: *AmazonRoute53_SimpleRoutingPolicy.png*
   * Providing the IP address associated with the specific domain name
2. Failover
   * Ref: *AmazonRoute53_FailOverRoutingPolicy.png*
   * If primary is down/failed (Based on health checks), routes to secondary destination
   * 設定哪個IP Address 是Primary，哪些是 Secondary，
   * Health checks need to enable if you need to use failover routing
3. Geolocation
   * Ref: *AmazonRoute53_GeolocationRoutingPolicy_V2.png*
   * Use geographic location you are in to route you to the closest region
   * Zone List will conclude A geo-location column, which save the IP belongs to which Region
      * *Default* Geolocation must be added in order to process the unknown location of DNS Query 
   * Health Check can be add into geolocation routing policy
4. Geoproximity
   * Route you to the closest region within a geographic area
   * Must create a policy in traffic flow
5. Latency
   * Ref: *AmazonRoute53_LatencyRoutingPolicy.png*
   * Directs you based on the **lowest latency** route to resource
6. Multivalue answer
   * Ref: *AmazonRoute53_MultiValueRoutingPolicy.png*
   * Returns several IP addresses and functions as a basic load balancer
7. Weighted
   * Ref: *AmazonRoute53_WeightedRoutingPolicy_V2.png*
   * Uses the relative weights assigned to resources to determine which to route to
   * 自訂比例，設定某百份比的DNS查詢流量回應某個record
8. IP-based
   * uses the IP addresses of clients to make routing decisions
### Features
1. Domain Registration
   * You can register your own public domain name using Amazon route 53
2. Health Checks
   * Route 53 can check your instances / load balances, whether they are healthy or not
3. Traffic Flow
   * A bit more logic in terms of how you direct traffic to different services


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
4. *Distribution*: Endpoints provided by CDN service, allow users to access the nearest edge server
  * name / access point of distribution & Multiple source of origin inside distribution
  * define behaviors (Path Pattern, Viewer Protocol Policy, Cache Policy, Origin Request Policy)
  * Currently **support web distrbition** only
    1. Speed up distrbution of static and dynamic content
    2. Distribute media files using HTTP and HTTPS
    3. Add, update, or delete object, and submit data from web forms
  * RTMP (~live streaming) is not supported since 2020
* Regional Edge Cache: sits between edge locations and the origin

## Advantages of usign CloudFront
1. Users can fetch data from the nearest edge server, resulting in much **faster access** speed and significantly improve user experience (使用者可以從最近的 edge server 拉資料，速度快多了，體驗自然大幅上升)
2. **Cost is lowered**, because the amount of data transmitted


## Reference
1. http://dns-learning.twnic.net.tw/bind/intro6.html (DNS Introduction)