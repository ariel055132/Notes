# Amazon Route 53
* Ref: *AmazonRoute53_How53Route.png*
* It is a highly available and scalable **DNS (Domain Name Service) web service**.
* It provide the following functions:
  1. *Domain Registration*: Allow domain name registration
  2. *Domain Name System (DNS) service*: Translate domains (e.g: ww.google.com) into IP address (192.169.0.0)
  3. *Health Checking*: Monitor the health of resources 
  4. *Security*: Support both DNSSEC for domain registration and DNSSEC signing

## Domain Registration


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