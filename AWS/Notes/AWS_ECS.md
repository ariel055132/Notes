# Amazon ECS 
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