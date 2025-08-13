# Test 3 - Question 10 
## Question
* A company has deployed an API in a VPC behind an internet-facing Application Load Balancer (ALB). An application that consumes the API as a client is deployed in a second account in private subnets behind a NAT gateway. When requests to the client application increase, the NAT gateway costs are higher than expected. A solutions architect has *configured the ALB to be internal*.
* Which combination of architectural changes will reduce the NAT gateway costs? (Choose two.)

## Option
* A. Configure a VPC peering connection between the two VPCs. Access the API using the private address.
* B. Configure an AWS Direct Connect connection between the two VPCs. Access the API using the private address.
* C. Configure a ClassicLink connection for the API into the client VPC. Access the API using the ClassicLink address.
* D. Configure a PrivateLink connection for the API into the client VPC. Access the API using the PrivateLink address.
* E. Configure an AWS Resource Access Manager connection between the two accounts. Access the API using the private address.

## Answer
* A. Configure a VPC peering connection between the two VPCs. Access the API using the private address.
* D. Configure a PrivateLink connection for the API into the client VPC. Access the API using the PrivateLink address.

## Explanation
* is a network connection between two VPCs that allows them to communicate using private IP addresses. By creating a peering connection between the client's VPC and the API's VPC, the client application can access the internal ALB via its private IP. This traffic stays within the AWS network and doesn't go through the NAT gateway, thus eliminating the associated costs.
* This technology enables you to privately access services hosted in a different VPC without using an internet gateway, NAT device, or VPC peering. You create a VPC endpoint in the client's VPC, and this endpoint provides a private IP address for the ALB in the other VPC. All traffic between the client and the API stays on the AWS network, bypassing the NAT gateway and reducing costs. PrivateLink is often preferred over VPC peering for service-oriented architectures because it simplifies network management and provides better security isolation.


* Why other options are incorrect:
    1. B. Configure an AWS Direct Connect connection between the two VPCs. Access the API using the private address: AWS Direct Connect is used for creating a dedicated private network connection from an on-premises data center to AWS, not for connecting two VPCs within AWS. This is the wrong tool for this task.
    2. C. Configure a ClassicLink connection for the API into the client VPC. Access the API using the ClassicLink address: ClassicLink is a deprecated feature that was used to link an EC2-Classic instance to a VPC. It is not relevant for modern VPC-to-VPC communication.
    3. E. Configure an AWS Resource Access Manager connection between the two accounts. Access the API using the private address: AWS Resource Access Manager (RAM) is a service for sharing AWS resources with other AWS accounts. It is used to share things like subnets, transit gateways, or RAM-supported resources, but it doesn't create a direct network connection for private IP communication in the way VPC peering or PrivateLink does.