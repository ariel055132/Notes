# Amazon Route 53
* Ref: *AmazonRoute53_How53Route.png*
* It is a highly available and scalable **DNS (Domain Name Service) web service**.
* It provide the following functions:
  1. *Domain Registration*: Allow domain name registration
  2. *Domain Name System (DNS) service*: Translate domains (e.g: ww.google.com) into IP address (192.169.0.0)
  3. *Health Checking*: Monitor the health of resources 
  4. *Security*: Support both DNSSEC for domain registration and DNSSEC signing

## Domain Registration (申請Domain Name)
1. The user will choose a domain and check that it is available to register
2. The user need to choose registrar to register the domain
3. The registrar check whether the domain name is available and pass all additional checks, and then It will provide registry with the details of the domain name
4. (After one year) the user can renew the domain name, otherwise the domain name is released. Others can purchase it.

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

## Health Checking
* Objective: monitor the health and performance of the underlying resources
* For a health check to succeed, the router and firewall rules must allow inbound traffic from the IP addresses that the health checkers use
* Health Checking Types are as follows:
    1. Monitor the *endpoint* (e.g web server / IP address)
    2. *Calculated* health checks
    3. Monitor the status of a *CloudWatch* alarm

### Health Checking Overall Procedure 
* Ref: *AmazonRoute53_HealthChecking.png*
1. User **create a health check** and specify values that define how the health check to work
2. Route 53 starts to **send the request to the endpoint** specified by user. If the endpoint responds to the request, Route 53 considers the endpoint to be *healthy* and do nothing.
3. If the **endpoint does not respond to request**, Route 53 starts to **count the number of consecutive requests** that the endpoint does not respond to:
   * If the count reaches failure threshold specified in health check, Route 53 considers the endpoint unhealthy
   * If the endpoint starts to respond again before the count reaches the failure threshold, Route 53 resets the count to 0. (Consider it is healthy)
4. If Route 53 considers the endpoint *unhealthy*, it **notifies CloudWatch**.
   * If user does not set up notification, the status of Route 53 health checks can be checked in the Route 53 console.
5. (Optional) If user configured notification for the health check, CloudWatch triggers an alarm and use Amazon SNS to send notification to specified users

### Routing Policy
1. Simple
   * Ref: *AmazonRoute53_SimpleRoutingPolicy.png*
   * A simple round-robin policy and can be applied when there is a single resource doing the function for the domain
   * Help configure **standard DNS records**, with no special Route 53 routing such as weighted or latency
   * does **not support health checks**
   * With Alias record enabled, only one AWS resource or one record can be specified in the current hosted zone
   * Providing the IP address associated with the specific domain name
2. Failover
   * Ref: *AmazonRoute53_FailOverRoutingPolicy.png*
   * Allows **active-passive failover configuration**
   * One resource (primary) takes all traffic when it's healthy and the other resource takes all traffic when the first is not healthy
   * **Health checks need to enable** if you need to use failover routing
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
   * Respond to DNS Query based on **which data center gives user the lowest network latency**
   * **Support health checks**
6. Multivalue answer
   * Ref: *AmazonRoute53_MultiValueRoutingPolicy.png*
   * Returns several IP addresses and functions as a basic load balancer
7. Weighted
   * Ref: *AmazonRoute53_WeightedRoutingPolicy_V2.png*
   * Uses the relative weights assigned to resources to determine which to route to (自訂比例，設定某百份比的DNS查詢流量回應某個record)
   * Weights can be assigned between **any number from 0 to 255 inclusive**
   * **Support health checks**
8. IP-based
   * uses the IP addresses of clients to make routing decisions
* *Failover routing* provides *active-passive configuration* for disaster recovery, while the others are *active-active configuration*


## Reference
1. https://jayendrapatil.com/aws-route-53/#AWS_Route_53
2. 