# Test 3 - Question 6
## Question
* An application hosted on AWS is experiencing performance problems, and the application vendor wants to perform an analysis of the log file to troubleshoot further. The log file is stored on Amazon S3 and is 10 GB in size. The application owner will *make the log file available to the vendor for a limited time*.
* What is the MOST secure way to do this?

## Option
* A. Enable public read on the S3 object and provide the link to the vendor.
* B. Upload the file to Amazon WorkDocs and share the public link with the vendor.
* C. Generate a *presigned URL* and have the vendor download the log file before it expires.
* D. *Create an IAM user* for the vendor to provide access to the S3 bucket and the application. Enforce *multi-factor authentication*.

## Answer
* C. Generate a presigned URL and have the vendor download the log file before it expires.

## Explanation
* D. Create an IAM user for the vendor to provide access to the S3 bucket and the application. Enforce multi-factor authentication.
  * This option grants the vendor an identity within your AWS environment. This is an unnecessary and significant security risk, as it *provides more access than is needed* (e.g., access to the entire S3 bucket, not just a single file) and *creates an administrative burden*. 
  * *The vendor would have long-term access, which goes against the requirement of making the file available for a limited time*.

## Thinking
* 就 Option C，Option D 之間在選
* Option A, B 不對是因為題目需要只把Log 給 vendor 看，public 代表所有人都能看，不符合題目需求