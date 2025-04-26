# CloudFront 
* CloudFront is a *CDN (Content Delivery/Distribution Network) service* provided by AWS through *edge servers deployed worldwide*. (AWS 透過建立在全世界各地的 edge server所提供的CDN服務)
* CloudFront delivers the content (static/dynamic web, streaming content) through *edge locations* or *Point of Presence (POP)*
* CloudFront speeds up the distribution of the content by *routing each user request to the edge locations* that can best serve the content, thus lowering latency
  * For example, if the user request is come from US, CloudFront will route the request to US edge locations instead of other edge location in order to speed up the distribution of the content.
* CloudFront uses the *AWS backbone network / AWS Global Network* that dramatically reduces the number of network hops that users' requests must pass through and helps improve performance, provide lower latency and higher data transfer rate

## Configuration and Content Delivery
* *Ref: source/CloudFront/AmazonCloudFront_ConfigurationAndContentDelivery.png*
1. **Origin servers** need to be configured to get the files for distribution.
   * It can be AWS hosted service (e.g S3, EC2), or an on-premise server
2. 

## Benefit
1. **Elminates the expense and complexity of operating network** of cache servers in multiple sites across the Internet
2. **Increase reliability and availability of resource access** because copies of objects are held in multiple edge locations around the world
3. **Keeps Persistent connections with the origin servers** (with the help of AWS backbone) so that files can be fetched from the origin servers as quickly as possible
4. Users can fetch data from the nearest edge server, resulting in much **faster access** speed and **significantly improve user experience** (使用者可以從最近的 edge server 拉資料，速度快多了，體驗自然大幅上升)
5. 

## Edge Locations & Regional Edge Caches
* Ref: *source/CloudFront/AmazonCloudFront_RegionalEdgeCaches.png*
* Edge Locations make sure that content can be served quickly to the viewers. (Because the physical distance between the edge location and users is shorter.)
* Regional Edge Caches are located between the Origin Servers and the Edge Locations, will support edge locations by providing the content if Cache miss happens in edge locations
* Regional Edge Caches support multiple edge locations

## Distribution
* Enpoints provided by CDN service, allow users to access the nearest edge server
* Support **Web distribution** only at the moment, RMTP is not support anymore
* Includes:
  1. S3 Origin / Custom Origin 
    * The location where content is stored, and from which CloudFront gets content to serve to viewers
  2. Behaviors
    * Path Pattern
    * Viewer Protocol
    * Cache Policy
    * Origin Request Policy

## Behaviors
1. Path Pattern
2. Viewer Protocol
3. Cache Policy
4. Origin Request Policy
### Path Patterns
* help define which path the Cache behaviour would apply to.
* A default (*) pattern need to be created and multiple cache distributions can be added with patterns to tak priority over the default path
### Viewer Protocol Policy (Viewer -> CloudFront)
* Define **the allowed access protocol to CloudFront** by define viewer protocol policy (哪些網路協定才能存取CloudFront內容)
1. HTTPS only - supports HTTPS only 

## CDN (Content Delivery/Distribution Network) 內容傳遞網路
* A geographically distributed network of proxy servers and their data centers
* Goals is to provide high availability and performance (low latency) by distributing the service spatially relative to end users