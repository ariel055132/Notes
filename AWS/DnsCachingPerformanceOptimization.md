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
   * Use geographic location you are in to route you to the closest region
4. Geoproximity
   * Route you to the closest region within a geographic area
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
* CloudFront is a *CDN service* provided by AWS through edge servers deployed worldwide. 
* It 
* *Origin*: The location where content is stored, and from which CloudFront gets content to serve to viewers
* Edge Location: Distributed around the world
* Distribution: What you create in cloudfront
  * name / access point of distribution & Multiple source of origin inside distribution
  * define behaviors (Path Pattern, Viewer Protocol Policy, Cache Policy, Origin Request Policy)
  1. Speed up distribution of static and dynamic content
  2. Distribute media files using HTTP and HTTPs
  3. Add from web forms
  4. Use live streaming to stream an event in real time
* Regional Edge Cache: sits between edge locations and the origin


## Reference
1. http://dns-learning.twnic.net.tw/bind/intro6.html (DNS Introduction)