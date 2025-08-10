# Test 3 - Question 23
## Question
* A company is hosting a web application on AWS using a single Amazon EC2 instance that stores user-uploaded documents in an Amazon EBS volume. For better scalability and availability, the company duplicated the architecture and created a second EC2 instance and EBS volume in another Availability Zone, placing both behind an Application Load Balancer. After completing this change, users reported that each time they refreshed the website, they could see one subset of their documents or the other, but never all of the documents at the same time.
* What should a solutions architect propose to *ensure users see all of their documents at once*? 

## Option
* A. Copy the data so both EBS volumes contain all the documents.
* B. Configure the Application Load Balancer to direct a user to the server with the documents.
* C. Copy the data from both EBS volumes to Amazon EFS. Modify the application to save new documents to Amazon EFS.
* D. Configure the Application Load Balancer to send the request to both servers. Return each document from the correct server.

## Answer
* C. Copy the data from both EBS volumes to Amazon EFS. Modify the application to save new documents to Amazon EFS.

## Explanation
* Why other options are incorrect:
  1. A. Copy the data so both EBS volumes contain all the documents.
    * A temporary fix
    * As soon as a new document is uploaded, it would be saved to only one of the EBS volumes, and the data would become out of sync again.
  2. B. Configure the Application Load Balancer to direct a user to the server with the documents.
    * The Application Load Balancer cannot determine which server has a specific user's documents without a complex and custom-built mechanism.
    * Furthermore, a user would still be unable to see all of their documents at once if they had uploaded some documents on each server.
  3. D. Configure the Application Load Balancer to send the request to both servers. Return each document from the correct server.
    * The Application Load Balancer is designed to forward a single request to a single target.
    * It does not have the capability to split a request, send it to multiple targets, and then combine the responses


## Thinking
* 其實 Option A 是一個暫時性可行的方法，只是每次都需要全部 Scan 兩個 EBS 的所有資料，並進行複製與對齊
* 這一題明顯是問 EFS 