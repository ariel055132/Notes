# Test 4 - Question 51
## Question
* A company wants to host a scalable web application on AWS. The application will be accessed by users from different geographic regions of the world. Application users will be able to download and upload unique data up to gigabytes in size. The development team wants a *cost-effective* solution to *minimize upload and download latency* and *maximize performance*.
* What should a solutions architect do to accomplish this?

## Option
* A. Use Amazon S3 with Transfer Acceleration to host the application.
* B. Use Amazon S3 with CacheControl headers to host the application.
* C. Use Amazon EC2 with Auto Scaling and Amazon CloudFront to host the application.
* D. Use Amazon EC2 with Auto Scaling and Amazon ElastiCache to host the application.

## Answer
* A. Use Amazon S3 with Transfer Acceleration to host the application.

## Explanation
* Option B is wrong as S3 with CacheControl would not provide low latency and network performance for uploads.
* Option C is wrong as *EC2 with Auto Scaling does not provide a cost-effective solution*. EC2 with Auto Scaling also needs to be fronted with a load balancer to work as the origin with CloudFront.
* Option D is wrong as ElastiCache is not an ideal solution to store this data. EC2 with Auto Scaling does not provide a cost-effective solution.


