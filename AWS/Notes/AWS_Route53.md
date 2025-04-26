# Amazon Route 53
* Ref: *source/AmazonRoute53/AmazonRoute53_How53Route.png*
* It is a highly available and scalable **DNS (Domain Name Service) web service**.
* It provide the following functions:
  1. **Domain Registration**: Allow domain name registration to hosted zone in *zone file*
  2. **Domain Name System (DNS) service**: 
      * Translate domains (e.g: ww.google.com) into IP address (e.g: 192.169.0.0)
      * Responds to DNS queries using a *global network* of authoritative DNS servers, which reduces latency
      * Route Internet traffic to CloudFront, Elastic Beanstalk, ELB, or S3. *No charges for DNS queries* to these resource.
  3. **Health Checking**: 
      * Monitor the health of resources 
      * *Sends automated requests over the Intenet to the application* to verify that it's reachable, available and functional
      * *CloudWatch alarms* can be configured for the health checks to sends notifications when a resource becomes unavailable
  4. **Security**: 
      * Support both *DNSSEC* for domain registration and DNSSEC signing

## Amazon Route 53 - Hosted Zone
* Container for records, which include information about **how to route traffic for a domain (such as example.com) and all of its subdomains (such as www.example.com, retail.example.com)**
* **Just finding the domain name**, but not its IPs
1. *Public Host Zone*
   * determines how traffic is routed on the **Internet**
   * It can be query if other are using the correct DNS server setting
2. *Private Hosted zone*
   * determines how traffic is routed within **VPC**
   * Need to set enableDnsHostname, enableDnsSupport to true

## Domain Registration (申請Domain Name)
1. The user will choose a domain and check that it is available to register
2. The user need to choose registrar to register the domain
3. The registrar check whether the domain name is available and pass all additional checks, and then It will provide registry with the details of the domain name
4. (After one year) the user can renew the domain name, otherwise the domain name is released. Others can purchase it.

## DNS (Domain Name System)
* Ref: *source/AmazonRoute53/DNS_Procedure.png*
* Objective
  * Converting a website entered by the user into the IP address of the web server they wish to connect to (將一般的英文網址轉換為電腦用的數字IP地址)
  * Input: domain name / website address (e.g: www.google.com)
  * Output: IP address of the domain name (to be precise, host server IP, e.g: 192.168.0.0)

### DNS Procedure
1. Users enters website address (aka. Domain Names) in browser, for example: www.google.com
2. DNS Server receive the domain names entered by user, it needs to resolved it to the IP address of the web server that the user wants to connect to
   * Each DNS server has a *zone file*, it contains lots of records that map the host name or the domain name to a value including IP addresses
   * DNS server is trying to map the domain name to the IP address, and return the IP to the user.
3. Computer connects to the IP addresses given by DNS Server

### DNS Zones and Records
1. A (IPv4 Address record) 
   * Maps a domain name to an IPv4 IP address (e.g google.com to 52.23.21.43)
2. AAAA (IPv6 Address record)
2. CNAME
   * Maps a domain name to another domain name (e.g google1.com to google2.com)
3. MX (Mail Exchange)
   * Returns the mail servers for a domain name
4. TXT (Text) Format
5. SRV

## Health Checking
* **Monitor the health and performance of the underlying resources**
* For a health check to succeed, the router and firewall rules must allow inbound traffic from the IP addresses that the health checkers use
* Health Checking Types are as follows:
    1. Monitor the *endpoint* (e.g web server / IP address)
    2. *Calculated* health checks
    3. Monitor the status of a *CloudWatch* alarm

### Health Checking Overall Procedure 
* Ref: *AmazonRoute53_HealthChecking.png*
1. User **create a health check** and specify values that define how the health check to work
   * *IP address* / domain name of the endpoint / CloudWatch alarm
   * The *protocol* (HTTP, HTTPS, GET) that you want Route 53 
   * *Failure threshold* (Consecutive times the endpoint must fail to respond to request before Route 53 considers it unhealthy)
   * *How to get notified* when Route 53 detect that the endpoint is unhealthy.
2. Route 53 starts to **send the request to the endpoint** specified by user. If the endpoint responds to the request, Route 53 considers the endpoint to be *healthy* and do nothing.
3. If the **endpoint does not respond to request**, Route 53 starts to **count the number of consecutive requests** that the endpoint does not respond to:
   * If the count reaches failure threshold specified in health check, Route 53 considers the endpoint unhealthy
   * If the endpoint starts to respond again before the count reaches the failure threshold, Route 53 resets the count to 0. (Consider it is healthy)
4. If Route 53 considers the endpoint *unhealthy*, it **notifies CloudWatch**.
   * If user does not set up notification, the status of Route 53 health checks can be checked in the Route 53 console.
5. (Optional) If user configured notification for the health check, CloudWatch triggers an alarm and use Amazon SNS to send notification to specified users

### Health Check Notes
* Why we need to use *CloudWatch Alarm*?
  * Since Route 53 Health Checks cannot monitor private endpoints. Therefore **monitoring private endpoints must be archieved by using CloudWatch Alarms instead**.
  1. Configure a CloudWatch Alarm to the private resources that need to be monitored.
  2. Create a Health Check to monitor this CloudWatch alarm for checking the healthy 
* Health checker how to evaluate the health of the endpoint?
  1. **Response time**
  2. **Specified failure threshold** - Whether the endpoint responds to a number of consecutive health checks (esp. for CALAULATED health check)
* Health check is considered healthy?
  1. HTTP, HTTPS & with String matching
      * TCP connection can be established within four seconds.
      * Returns 2xx or 3xx within two seconds after connecting
      * Route 53 searches the response body for the specified string which must appear entirely in the first 5,120 bytes of the response body or the endpoint fails the health check.
      * (More precise) If more than 18% of the responses are normal, it will be marked as healthy. Otherwise, unhealthy.
  2. TCP
      * TCP connection can be established within ten seconds.
  3. CALCULATED
      * It will **monitor the status of other health checks**.
      * Route 53 adds up the number of health checks that Route 53 health checkers considered to be healthy.
      * Compare the number of health check is greater than the value of HealthThreshold.
      * If greater, it is considered as healthy. Otherwise, unhealthy.
      * It can be used to perform **maintenance of the website system** without causing all health checks to fail
  4. CLOUDWATCH_METRIC
      * Check the health of the **CloudWatch alarm**.
      * If the state of the alarm is **OK**, the health check is considered **healthy**.
      * If the state is **ALARM**, the health check is considered **unhealthy**.
      * If CloudWatch does **not have sufficient data to determine whether the state** is OK / ALARM, the health check status depends on the **setting for InsufficientDataHealthStatus**: Healthy, Unhealthy, or LastKnownStatus

## Routing Policy
1. Simple
   * Ref: *AmazonRoute53_SimpleRoutingPolicy.png*
   * A **round-robin** policy and can be applied when there is a single resource doing the function for the domain (最基本的 routing，只看 zone list 上的記錄來給 IP，若zone list 上有多個相同 domain name 的 IP，則透過隨機的方式來給 IP)
   * Help configure **standard DNS records**, with no special Route 53 routing such as weighted or latency
   * does **not support health checks**
   * With Alias record enabled, only one AWS resource or one record can be specified in the current hosted zone
   * Providing the IP address associated with the specific domain name
2. Failover
   * Ref: *AmazonRoute53_FailOverRoutingPolicy.png*
   * Allows **active-passive failover configuration**
   * One resource (primary) takes all traffic when it's healthy and the other resource takes all traffic when the first is not healthy (檢查Primary的server是否健康，若為否，呼叫Secondary的server)
   * **Health checks need to enable** if you use failover routing
3. Geolocation
   * Ref: *AmazonRoute53_GeolocationRoutingPolicy_V2.png*
   * Use *geographic location* you are in to route you to the closest region (按照地理位置來進行 routing)
   * Zone List will conclude A *geo-location column*, which save the IP belongs to which Region
      * *Default* Geolocation must be added in order to process the unknown location of DNS Query 
   * Health Check can be add into geolocation routing policy
4. Geoproximity
   * Route you to the closest region within a geographic area
   * Must create a policy in traffic flow
5. Latency
   * Ref: *AmazonRoute53_LatencyRoutingPolicy.png*
   * Respond to DNS Query based on **which data center gives user the lowest network latency** (根據網路傳送延遲來判斷，往延遲低的地方送)
   * **Support health checks**
6. Multivalue answer
   * Ref: *AmazonRoute53_MultiValueRoutingPolicy.png*
   * Returns several IP addresses and functions as a basic load balancer
   * **Support Health Checks**, only the values for healthy resources are returned
7. Weighted
   * Ref: *AmazonRoute53_WeightedRoutingPolicy_V2.png*
   * Uses the relative weights assigned to resources to determine which to route to (自訂比例，設定某百份比的DNS查詢流量回應某個record)
   * Weights can be assigned between **any number from 0 to 255 inclusive**
   * **Support health checks**
8. IP-based
   * uses the IP addresses of clients to make routing decisions
* Conclusion:
  * *Active-Passive Configuration*
    * Involves a **primary active system** and a **secondary passive system** that remains inactive until the primary system fails
    * Primary active system handles all incoming requests while the passive system remains on standby, ready to take over if the primary system encounters a failure or becomes unavailable
    * **Redundancy and reliability**
  * *Active-Active Configuration*
    * **Multiple identical resources are simultaneously active and serving requests** 
    * Incoming requests are distributed across all active resources
    * **Load Balancing and maximizing resource utilization -> High Availability**
  * 只有 Simple Routing Policy 不支援 Health Checking，其他 Routing Policy 都支援 Health Checking
  * 只有 failover routing 是 active-passive configuration，其他的 routing 都是 active-active configuration

## Traffic Flow
* Objective: 
  1. Allow users to create routing configuration for resources
  2. Track the related records and relationships in a hosted zone
* It also includes a **versioning** feature that allows you to maintain a history of changes to your routing policies
* Easily **roll back** to a previous policy version using the console or API

## Route 53 Resolver
* Automatically answers DNS queries for
1. Local VPC domain names for EC2 instances
2. Records in private hosted zones
3. Performs recursive lookups against public name servers in the internet for public domain names
* When we need? 
  * Because the development environment maybe hybrid.
### Inbound Endpoint
* Allow DNS queries to your VPC from your on-premises network or another VPC
* all the result is returned by Route 53 via the inbound endpoint
* 讓外部環境中的資源查詢AWS內部資源用

### Outbound Endpoint
* Allow DNS queries from your VPC to your on-premises network or another VPC
* All the result is returned by Route 53 via the outbound endpoint
* 讓AWS內部資源查詢外部資源用

### Resolver Rule
* Use this to control how DNS query is transfered to DNS resolver
1. Conditional Forwarding Rules
   * Used to specify which domain name queries should be forwarded to which DNS server.
2. System Rules
   * (Optional) Overwrite/override the rules above.
3. Auto-defined System Rules
   * For AWS domain or private hosted zone 

## DNSSEC 

## QA
1. You have deployed a web application targeting a global audience across multiple AWS Regions under the domain name example.com. You decide to use Route 53 Latency-Based Routing to serve web requests to users from the region closest to the user. To provide business continuity in the event of server downtime you configure weighted record sets associated with two web servers in separate Availability Zones per region. During a DR test you notice that when you disable all web servers in one of the regions Route 53 does not automatically direct all users to the other region. What could be happening? (Choose 2 ans)

## Quiz
1. A company provides videos for new employees around the world. They need to store the videos in one location and then provide low-latency access for the employees around the world. Which service would be best suited to providing fast access to the content?
   * Use Amazon CloudFront
2. An Architect is designing a web application that has points of presence in several regions around the world. The Architect would like to provide automatic routing to the nearest region, with failover possible to other regions. Customers should receive 2 IP addresses for whitelisting. How can this be achieved?
   * Use AWS Global Accelerator
3. Which of the following are NOT valid origins for Amazon CloudFront?
   * AWS Lamdba Function
4. An Architect needs to point the domain name dctlabs.com to the DNS name of an Elastic Load Balancer. Which type of record should be used?
   * Alias Record
5. A company hosts copies of the same data in Amazon S3 buckets around the world and needs to *ensure that customers connect to the nearest S3 bucket*. Which Route 53 routing policy should be used?
   * Latency Routing Policy 
   * The latency routing policy directs based on the lowest latency to the AWS resource.
   * Latency increases over distance so this ensure customers connect to the closest S3 bucket
6. A media organization *offers news in local languages* around the world. Which Route 53 routing policy should be used to direct readers to the website with the correct language?
   * Geolocation Routing Policy
   * Need to identify specific geographic locations and associate them with the correct language version
7. Which routing policy would you use to *route to a secondary destination* in the event a *primary is down*?
   * Failover Routing Policy
   * It based on health checks and will route to a secondary destination when the primary is down

## Reference
1. https://jayendrapatil.com/aws-route-53/#AWS_Route_53 (Route 53)
2. https://www.geeksforgeeks.org/active-active-vs-active-passive-architecture/ 
3. https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver.html (Resolver)