# AWS DNS, Caching, and Performance Optimization
* Introduction of the following setting
* Amazon Route 53: DNS Server
* Amazon CloudFront: Content delivery network
* AWS Global Accelerator: similar as Amazon CloudFront

## DNS (Domain Name System)
* Objective
  * Converting a website entered by the user into the IP address of the web server they wish to connect to
* How
  1. Each DNS server has a *zone file*, it contains lots of records that map the host name or the domain name to a value including IP addresses
  2. Computer can connect to the IP addresses with the help of zone file

## Amazon Route 53
* An advanced DNS (with more routing policy)
### Routing Policy
1. Simple
   * Providing the IP address associated with the specific domain name
2. Failover
   * If primary is down/failed (Based on health checks), routes to secondary destination
3. Geolocation
   * Use geographic location you are in to route you to the closest region
4. Geoproximity
   * Route you to the closest region within a geographic area
5. Latency
   * Directs you based on the lowest latency route to resource
6. Multivalue answer
   * Returns several IP addresses and functions as a basic load balancer
7. Weighted
   * Uses the relative weights assigned to resources to determine which to route to
8. IP-based
   * uses the IP addresses of clients to make routing decisions
### Features
1. Domain Registration
   * You can register your own public domain name using Amazon route 53
2. Health Checks
   * Route 53 can check your instances / load balances
3. Traffic Flow
   * A bit more logic in terms of how you direct traffic to different services