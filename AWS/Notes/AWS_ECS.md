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
* Managed service for running *Kubernetes applications* in the *cloud / on-premises*
  * Kubernetes: Open-source system for automating deployment, scaling, and management of containerized applications
* Use when you need to *standardize container* orchestration across multiple environments using a *managed Kubernetes* implementation

### Use Cases
1. Batch processing
   * Running sequential / batch workloads on EKS cluster using the Kubernetes Jobs API
2. Machine Learning 
   * Use Kubeflow with EKS to model machine learning
3. Web Applications
   * Build web applications that automatically scale up / down, run in a highly available configuration across multiple Availability Zones
4. Hybrid Deployment
   * Manage Kubernetes clusters and applications across hybrid environments (AWS + On-premises)

### Workload Auto Scaling
1. Vertical Pod AutoScaler
   * Automatically **adjusts the CPU and memory reservations** for your pods to help "right size" your applications (*Scaling up*) * Ref: AWS_ElasticLoadBalancingAndAutoScaling.md

2. Horizontal Pod AutoScaler
   * Automatically **scales the number of pods in a deployment**, replication controller, or replica set based on that resource's CPU utilization (*Scaling Out*)
   * Ref: AWS_ElasticLoadBalancingAndAutoScaling.md

### AutoScaling Product
1. *Kubernetes Cluster Autoscaler* uses *AWS scaling groups*
2. *Karpenter open source autoscaling project* uses *Amazon EC2 fleet*

### More
* EKS support Network Load Balancers & Application Load Balancers
* *AWS Load Balancer Controller* manages *AWS Elastic Load Balancers* for a Kubernetes cluster
* Installs the AWS Load Balancer Controller using Helm V3 / applying a Kubernetes manifest
1. Create a Kubernetes Ingress -> Application Load Balancer (ALB)
2. Kubernetes service LoadBalancer -> Network Load Balancer (NLB)
* With the AWS Load Balancer Controller version 2.3.0 or later, you can create NLBs using either target type

### EKS Distro
* Distribution of Kubernetes with the same dependencies as Amazon EKS
* Allow you to *manually run Kubernetes clusters anywhere*
* Includes binaries and containers of open-source Kubernetes, etcd, networking, and storage plugins, *tested for compatibility*
* Users can *securely access EKS Distro releases* as open source on GitHub or within AWS via Amazon S3 and Amazon ECR
*  Users can create Amazon EKS Distro clusters in AWS on Amazon EC2 and and on your own on-permieses hardware using the tooling of your choice
* Amazon EKS Distro *alleviates the need to track update, determine compatibility, and standardize on a common Kubernetes version across distributed teams*

### ECS and EKS Anywhere
* Run ECS / EKS on customer-managed infrastructure, supported by AWS
* Customer can run their own on-premises infra on bare metal servers
* deploy ECS/EKS Anywhere using VMware vSphere

## Elastic Container Registry (ECR)
* *fully-managed container registry*, integrated with Amazon ECS and Amazon EKS
* Container images and artifacts are stored in S3
* Can use Docker tools and Docker CLI commands such as push, pull, list, and tag
* Can be accessed from any Docker environment - in the cloud, on-premises, or on your machine
* Public Repositories allow everyone to access container images
* Access Control applies to private repositories
  1. IAM Access Control: Set policies to define access to container images in private repositories
  2. Resource-based policies: Access control down to the individual API actions
* 想像成 harbor

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

### Other ECR Features
1. Lifecycle policies
   * Manage the lifecycle of the images in your repositories (管理 images 的存活週期)
2. Image Scanning
   * Identify software vulnerabilities in container images (弱掃)
3. Cross-Region and Cross-Account Replication
   * Replicate images across accounts / region
4. Pull through cache rules
   * Cache repositories in remote public registries in your private Amazon ECR registry

## App Runner
* Fully managed service for deploying containerized web apps and APIs