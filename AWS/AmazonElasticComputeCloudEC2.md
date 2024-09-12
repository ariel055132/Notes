# Amazon ELastic Compute Cloud EC2


## Objectives



## What is EC2?
* A service in which we can run EC2 instances (virtual servers come with different combinations of CPU, memory, storage, and networking)
* *AWS* manage EC2 host, while *EC2 host server* manage *EC2 instances*

## Public, Private, and Elastic IP address
### Public IP address
* Associated with a private IP address on the instance
* Lost when the instances is closed/stopped, another new public IP address is gained.
* Used in public subnets
* Free to use them.
* Cannot be moved between instances (because it will lose when you are trying to move the address.)

### Private IP address
* Retained when the instance is stopped
* Used in Public and Private Subnets

### Elastic IP address
* static public IP address.
* charged even you are not using
* Associated with a private IP address on the instance.
* Can be moved between instances and Elastic network adapters.