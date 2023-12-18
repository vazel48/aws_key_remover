# aws_key_remover

Q:
My company has a team of developers that provisions their own resources on the AWS cloud. The developers use IAM user access keys to automate their resource provisioning and application testing processes in AWS. 
To ensure proper security compliance, the security team wants to automate deactivating and deleting any IAM user access key over 90 days old.
We need a solution with the LEAST operational effort.

A:
Use the AWS Config managed rule to check if the IAM user access keys are not rotated within 90 days. 
Create an Amazon EventBridge (Amazon CloudWatch Events) rule for the non-compliant keys, and define a target to invoke a custom Lambda function to deactivate and delete the keys.
