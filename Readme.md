

This repo contains 
- Code for the xls parser
- AWS Lambda function + test input event as json
- Test case(s) and data folder containing test data

It does not contain the xlrd libraries which are required by AWS Lambda to be present in the same directory.

This solution is created as a AWS lambda function which is invoked on upload to an S3 bucket.
The input is parsed and output generated to another bucket.

The solution file is at this url  http://s3.us-east-2.amazonaws.com/steel-bucket-out/ISO10383_MIC.json
