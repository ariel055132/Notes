# Amazon ECS (Elastic Cloud Service)
* Allows us to run container on AWS

## Docker Containers and Microservices
* Microservices architecture
    * Applications are structured as a collection of loosely coupled, independently deployable services, each running its own process
    1. Using API (Application Programming Interfaces) -> Easier integrations between application components; assists with loose coupling 
    2. Independently deployable blocks of code -> Can be scaled and maintained independently

### Server virtualization vs Containers
1. Server virtualization (Aka. EC2 Instance)
   * Create multiple VMs on a physical host
   * Each VM runs its own operating system
   * More resource-intensive, each VM needs complete OS and hardware
2. Container
   * Share the host OS kernel (Lightweight)
   * runs the application in container, which includes all the code, settings, and dependencies for running the application
   * Utilizes containerization to package an application and its dependencies into a *docker image* (Think as AMI)
   * Provides a cloud-based registry service for sharing container images and automating workflows via *Docker Hub* 

### Microservices: Attributes and Benefits
1. Use of Application Programming Interfaces (APIs)
   * Easier integrations between application components;
   * assists with loose coupling
     * Failure isolation
     * independent deployment
2. Independently deployable blocks of code
   * Can be scaled and maintained independently
3. Business-oriented architecture
   * Deployment organized around business capabilities
   * Team may be cross-functional and services may be reused
4. Flexible use of technologies
   * Each microservice can be written using different technologies
5. Speed and agility
   * Fast to deploy and update
   * Easy to include high availability and fault tolerance for each microservice

## Elastic Container Service (ECS)


## Auto Scaling
1. Service auto scaling
   * Automatically adjusts the desired task count up or down using the Application Auto Scaling Service
   * Supports target tracking, step and scheduled scaling services
2. Cluster auto scaling
   * Use a capacity provider to scale the number of EC2 Cluster instances using EC2 Auto Scaling
   * Uses an EC2 resource type called a Capacity Provider
   * A capacity provider can be associated with an EC2 Auto Scaling Group (ASG)

### Target Tracking Scaling Policies
* Increases or decrease the number of tasks that your service runs based on a target value for a specific CloudWatch Metric
* For example, if metric performance is > 80 is set

### Step Tracking Policies


### Scheduled Scaling 


## Elastic Kubernetes Service (EKS)
* Managed service for running Kubernetes applications in the cloud / on-premises
* Hybrid Development: clusters across AWS / On-premises
* Batch processing: running sequential / batch workloads on EKS cluster using the Kubernetes Jobs API
* Machine Learning: Use Kubeflow with EKS to model machine learning
* Web Applications: Build web applications that automatically scale up / down, run in a highly available configuration across multiple Availability Zones


### Workload Auto Scaling
1. Vertical Pod AutoScaler
   * Automatically **adjusts the CPU and memory reservations** for your pods to help "right size" your applications (*Scaling up*, Ref: AWS_ElasticLoadBalancingAndAutoScaling.md)

2. Horizontal Pod AutoScaler
   * Automatically **scales the number of pods in a deployment**, replication controller, or replica set based on that resource's CPU utilization (*Scaling Out*, Ref: AWS_ElasticLoadBalancingAndAutoScaling.md)

### AutoScaling Product
* Kubernetes Cluster Autoscaler -> AWS scaling groups
* Karpenter open source autoscaling project -> Amazon EC2 fleet

### More
* EKS support Network Load Balancers & Application Load Balancers
* *AWS Load Balancer Controller* manages *AWS Elastic Load Balancers* for a Kubernetes cluster
* Installs the AWS Load Balancer Controller using Helm V3 / applying a Kubernetes manifest
1. Create a Kubernetes Ingress -> Application Load Balancer (ALB)
2. Kubernetes service LoadBalancer -> Network Load Balancer (NLB)

### EKS Distro
* Distribution of Kubernetes with the same dependencies as Amazon EKS
* Allow you to manually run Kubernetes clusters anywhere

### ECS and EKS Anywhere
* Run ECS / EKS on customer-managed infrastructure, supported by AWS
* Customer can run their own on-premises infra on bare metal servers
* deploy ECS/EKS Anywhere using VMware vSphere

## Elastic Container Registry (ECR)
* fully-managed container registry
* Container images and artifacts are stored in S3
* Public Repositories allow everyone to access container images
* Access Control applies to private repositories
  1. IAM Access Control: Set policies to define access to container images in private repositories
  2. Resource-based policies: Access control down to the individual API actions

### Components
1. Registry
   * Amazon ECR private Registry is provided to each AWS account
   * You can create one or more repositories in your registry and store images in them
2. Authorization token
   * Use it to authenticate to ECR registries as an AWS user before it can push and pull images
3. Repository
   * contain Docker images, OCI images, OCI compatible artifacts
4. Repository Policy
   * Control access to repositories and the images within them
5. Image
   * push and pull images to your repositories