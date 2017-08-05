a) Mail Receiving Design:

- Configure the AWS Simple Email Service (SES) to receive emails 
- Create the S3 bucket 
- Cofigure logs of receiving email to S3 bucket
- Configure the SES to save to S3

Optional:

 - configure to send emails
 - configure domian name
 
b) Parser - Lambda Function
- triggered from S3 upload event 
- parse email body to extract 4 fileds:
  - upper block of text 
  - sender email 
  - sender name 
  - timestamp recieved
- insert into database

c) Database:
- [DynamoDB](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) 
- Mongo?

d) Admin web frontend (flask/[ebtalk][ebt] or ec2)
More here (EP): list actions taken by Admin 

e) User web frontend (flask/[ebtalk][ebt] or ec2)
More here (EP): list actions taken by Admin

[ebt]: https://aws.amazon.com/ru/elasticbeanstalk/

Use [AWS Cognito User Pool](http://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html) for the user authentication.

> Cognito is best option which for the sign up/ sign in/ with user data, FB/TW or other social accounts with JWT tokens
> Other option is store the user data to database and validate those.
 
 Testing
 -------
 
 - <https://github.com/spulec/moto>: a library that allows your python tests to easily mock out the boto library
 - mocking out a database? <https://stackoverflow.com/questions/145131/whats-the-best-strategy-for-unit-testing-database-driven-applications>
 
 
Comments
-------- 
 
Application Infrastructre:

1. Create the Elastic Beanstalk web application with Python platform. Upload your application flask code.
3. Create the environments like test, development, staging, production etc.
3. Create the new database and configure that with EBS web application.
4. Whenever there will be code changes, need to deploy the EBS.
5. If require, we can add the custom domain setting for the EBS url.


Application Features:

```
1 Admin:
1.1 Authenticate the Admin user (Authentication will be done with the AWS Cognito User pool)
1.2 Edit / Delete / stage for View the Resumes data stored in S3/Database.

2 User:
2.1 See the front page with authorization (Authentication will be done with the AWS Cognito User pool)
2.2 List of the resume data from database
```
