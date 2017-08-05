a) Mail Receiving Design:

1 Configure the AWS Simple Email Service (SES) to receive emails 
2 Create the S3 bucket 
3 Cofigure logs of receiving email to S3 bucket
4 Configure the SES to save to S3

Optional:
 - configure to send emails
 - configure domian name
 
b) Parser - Lambda Function
- Triggered from S3 upload event 
- parse email body to extract 4 fileds:
  - upper block of text 
  - sender email 
  - sender name 
  - timestamp recieved
- insert into database.

c) Database:
 - TODO (Vijay): which one and where is hosted
 
d) Admin web frontend (flask/eb)
 - NOT TODO. need API for this? 

e) User web frontend (flask/eb)
 - NOT TODO. need API for this?
 
*) Authentication Mechanism:   
 - AWS Cognito User Pool for the user authentication. http://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html
 - TODO (Vijay): other options? are they needed?
 
Comments
-------- 
 
Application Infrastructre:
1 Create the Elastic Beanstalk web application with Python platform. Upload your application flask code.
2 Create the environments like test, development, staging, production etc.
2 Create the new database and configure that with EBS web application.
3 Whenever there will be code changes, need to deploy the EBS.
4 If require, we can add the custom domain setting for the EBS url.
5 Create the AWS Cognito User Pool for the user authentication. http://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html


Application Features:
1 Admin:
1.1 Authenticate the Admin user (Authentication will be done with the AWS Cognito User pool)
1.2 Edit / Delete / stage for View the Resumes data stored in S3/Database.

2 User:
2.1 See the front page with authorization (Authentication will be done with the AWS Cognito User pool)
2.2 List of the resume data from database

