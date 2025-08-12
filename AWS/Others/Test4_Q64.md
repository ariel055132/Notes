# Test 4 - Question 64
## Question
* A company is processing data on a daily basis. The results of the operations are stored in an Amazon S3 bucket, *analyzed daily for one week*, and then must *remain immediately accessible* for occasional analysis.
* What is the MOST cost-effective storage solution alternative to the current configuration?

## Option
* A. Configure a lifecycle policy to delete the objects after 30 days.
* B. Configure a lifecycle policy to transition the objects to Amazon S3 Glacier after 30 days.
* C. Configure a lifecycle policy to transition the objects to Amazon S3 Standard-Infrequent Access (S3 Standard-IA) after 30 days.
* D. Configure a lifecycle policy to transition the objects to Amazon S3 One Zone-Infrequent Access (S3 One Zone-IA) after 30 days.

## Answer
* C. Configure a lifecycle policy to transition the objects to Amazon S3 Standard-Infrequent Access (S3 Standard-IA) after 30 days.

## Thinking
* 請審題，glacier 的 accessible 不會是 immediately，都需要一點時間才能獲取
* 因此 Option B 不會是正確