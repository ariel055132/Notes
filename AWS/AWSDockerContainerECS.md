# Docker Container and ECS
1. Docker container
   * Run application with fewer underlying resources and dependencies
2. ECS (Elastic Container Service)
  * Service allows us to run docker container on AWS
  * Elminates the need to install, operate, and scale 

## ECS Component
1. Cluster: Logical grouping of tasks or service
2. Container instance: EC2 instance running the ECS agent
   * IAM role provides permission to the host
   * ECS task IAM role provides permissions to the container
3. Task Definition: Blueprint that describes how a docker container should launch
4. Task: A running container using settings in a task definition
5. Image: Image refered in the task definition
6. Service: Defines long running tasks
### Docker Containers, Images
1. *Docker Container*
   * a standarized unit of software development
   * Containing everything that software application needs to run
   * lightweight because they share the host system's kernel
   * ideal for **microservices** architectures and building **cloud-native** applications
2. *Image*
   * Instructions for creating a Docker container
   * built from a **Dockerfile**
   * stored in a **registry** (E.G docker hub, ECR...) from which they can be downloaded and run on the container instances
* Application deployed on ECS must be architected to run in **Docker containers**
* **Amazon Elastic Container Registry (ECR)** is a managed AWS Docker registry service 
* Use **Docker CLI** to push, pull and manage images

### Cluster
* A logical grouping of EC2 container instances to run tasks or services
* ECS download the container images from the specified registry, and runs those images on the cluster instances

### Task and Task Definition
1. *Task*
2. *Task Definition*
   * A description of an application that container one or more docker containers
   * Required to prepare an application to run on ECS
   * A text file in JSON format, up to a maximum of 10
   * Specify various parameters for the application
      1. Containers to use
      2. Repositories
      3. Ports to be opened
      4. Data Volumes

## ECS and IAM roles (Not Completed)
1. Amazon ECS container instance IAM role
   * used by EC2 and external instances to provide permissions to the container agent to **call AWS APIs**
2. Task IAM role
   * Permission granted in IAM role are assumed by the containers running in the task
3. Amazon ECS task execution IAM role
   * Grants 
4. Amazon ECS infrastructure IAM role
   * Allow Amazon ECS to manage infrastucture resources in your clusters on your behalf

## ECS Scaling
1. Service Auto Scaling
   * Automatically adjusts the desired task count up or down using the Application Auto Scaling Service
   * Supports target tracking, step, and scheduled scaling policies
2. Cluster Auto Scaling
   * Uses a Capacity Provider to scale the number of EC2 cluster instances using EC2 Auto Scaling

## AWS EC2 Launch Type
* **Configure and deploy EC2 instances in cluster** to run containers 
* Charged for per running EC2 instance, not for the task
* Handle the cluster optimization by yourself
* Suitable for following
  1. Workloads that require consistently high CPU core and memory usage
  2. Large workloads that need to be optimized for price
  3. Applications need to access persistent storage
  4. directly manage your infrastructure

## AWS Fargate Launch Type
* **Serverless pay-as-you-go option** with Amazon ECS to run containers without having to manage servers or clusters of Amazon EC2 instances
* No need to manage the cluster by yourself, means that it is difficult to scale / optimize the cluster
* Charged for running task
* Suitable for following
  1. Large workloads that need to be optimized for low overhead
  2. Small workloads that have an occasional burst
  3. Tiny workloads
  4. Batch workloads

## Note: Microservices architecture
* Applications are structured as a collection of **loosely coupled**, independently deployable services, each running its own process
* features
1. Use **API** for communication
   * Easier integrations and communications between application components
   * assist with loose coupling
2. **Independently** deployable blocks of code
   * Can be scaled and maintained independently
3. Business-oriented architecture
   * Deployment organized around business capabilities
   * teams may be cross-functional and services may be resued
4. **Flexible use of technologies**
   * Each microservice can be written using different technologies 
   * No need to worry about communication because of APIs
5. **Speed and agility**
   * Fast to deploy and update.
   * Easy to include high availability and fault tolerance for each microservice
