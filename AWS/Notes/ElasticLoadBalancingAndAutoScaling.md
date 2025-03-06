# Elastic Load Balancing, and Auto Scaling

* Objectives
  * How to make sure that applications have enough capacity, enough EC2 instances available
  * How to distribute incoming connections to those EC2 instance?
  * --> Form Elastic and Fault Tolerant applications


* Definition
  1. Load Balancing: Distribute the connections across the pool of instances that are managed by the Auto Scaling Group
  2. Auto Scaling: make sure that you have the right number of EC2 instances to service the demand


* Stateful and Stateless applications
  1. Stateful
    * Maintain the state of the interaction. 
    * E.G: Web applications like facebook
  2. Stateless
    * Does not retain information about previous interactions. Each interaction is independent of others
    * E.G: Weather website

* Scaling up vs Scaling out
  1. Scaling up (Vertical Scaling)
    * Adding more resources to a single machine or server 
  2. Scaling out (Horizontal Scaling)
    * Adding more machine or node to the system
    * More preferred in cloud (raise flexibility and availability)

* Auto Scaling Group (ASG)
    * Automatically launches and terminates instances when instances need to be replaced or need to increase or decrease the capacity of cluster
    * Maintain availability and scale capacity
    * Integrates with AWS services
        1. Cloudwatch -> monitoring and scaling
        2. Elastic Load Balancing -> distributing connections
        3. EC2 Spot Instances option -> Cost Optimizations
        4. Amazon VPC -> deploying instances across AZs
    * Automatic Scaling
        * Instances are sending information to CloudWatch.
        * If the metric report that the nodes have in aggegate exceeded 80% utilization of their CP Uses.
        * Cloudwatch can notify auto scale to add a new node (**Scaling Out**), terminate the instances when utilization decreases
    * Maintaining availability
        * Instances are sending information to CloudWatch.
        * The report can reveal the status of the instances
        * If the status is failed, ASG will replace it.
    * Config
        1. Launch Template 
            * Specifies the EC2 instance configuration
        2. Configure purchase options
        3. Configure VPC and Subnets
        4. Attach Load Balancer
        5. Configure health checks EC2 & ELB
           * EC2: EC2 status checks
           * ELB: ELB (Load Balancing) health checks in addition to EC2 status checks
           * Health Check grace period: How long to wait before checking the health status of the instance
        6. Group Size and Scaling Policies
        7. Types
           * Manual
           * Dynamic: automatically scales based on demand 
           * Predictive: use Machine Learning algorithms to predict
           * Scheduled: based on a schedule