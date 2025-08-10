# Test 3 - Question 17
## Question
* A company provides a *Voice over Internet Protocol (VoIP) service* that uses *UDP connections*. The service consists of Amazon EC2 instances that run in an Auto Scaling group. The company has *deployments across multiple AWS Regions*. The company needs to *route users to the Region with the lowest latency*. The company also needs *automated failover between Regions*.
* Which solution will meet these requirements?

## Option
* A. Deploy a *Network Load Balancer (NLB)* and an associated target group. Associate the target group with the Auto Scaling group. Use the NLB as an *AWS Global Accelerator* endpoint in each Region.
* B.  Deploy an Application Load Balancer (ALB) and an associated target group. Associate the target group with the Auto Scaling group. Use the ALB as an AWS Global Accelerator endpoint in each Region.
* C. Deploy a *Network Load Balancer (NLB)* and an associated target group. Associate the target group with the Auto Scaling group. Create an *Amazon Route 53 latency record* that points to aliases for each NLB. Create an *Amazon CloudFront distribution* that uses the latency record as an origin.
* D. Deploy an Application Load Balancer (ALB) and an associated target group. Associate the target group with the Auto Scaling group. Create an Amazon Route 53 weighted record that points to Pliqses for each ALB. Deploy an Amazon CloudFront distribution that uses the weighted record as an origin.

## Thinking
* 看到 UDP connections，基本上用 Network Load Balancer (NLB)，所以排除 Option B & Option D

## Explanation
* Option C incorrect:
  * While Route 53 latency records can route traffic based on latency, this approach relies on DNS, which can be affected by caching.
  * More importantly, **CloudFront is a Content Delivery Network (CDN) and is designed for caching web content (HTTP/S)**
  * **Not designed to handle a real-time, UDP-based VoIP service**.