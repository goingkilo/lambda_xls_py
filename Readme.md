

This repo contains 
- Code for the xls parser (xls_processor.py)
- AWS Lambda function + test input event as json + yaml file (lambda_handler.py, test_input.json, steel-eye-processor.yaml)
- Test case(s) and data folder containing test data (data/ISO10383_MIC.xls, data/dummy.xls)

It does not contain the xlrd libraries which are required by AWS Lambda to be present in the same directory.

This solution is created as a AWS lambda function which is invoked on upload to an S3 bucket.
The input is parsed and output generated to another S3 bucket.

The solution file is generated at this url  http://s3.us-east-2.amazonaws.com/steel-bucket-out/ISO10383_MIC.json
