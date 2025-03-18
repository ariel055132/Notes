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
