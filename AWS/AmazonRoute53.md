# Amazon Route 53
* Ref: *AmazonRoute53_How53Route.png*
* It is a highly available and scalable **DNS (Domain Name Service) web service**.
* It provide the following functions:
  1. *Domain Registration*: Allow domain name registration
  2. *Domain Name System (DNS) service*: Translate domains (e.g: ww.google.com) into IP address (192.169.0.0)
  3. *Health Checking*: Monitor the health of resources 
  4. *Security*: Support both DNSSEC for domain registration and DNSSEC signing

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
* monitor the health and performance of the underlying resources
* For a health check to succeed, the router and firewall rules must allow inbound traffic from the IP addresses that the health checkers use
* Health Checking Types are as follows:
    1. Monitor the *endpoint* (e.g web server / IP address)
    2. *Calculated* health checks
    3. Monitor the status of a *CloudWatch* alarm