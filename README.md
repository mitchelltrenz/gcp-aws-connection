# gcp-aws-connection
The following steps can be followed to create an automated push of files from GCP Storage to AWS S3.
In this particular example, the following products are utilized: 2 GCP Storage Buckets (original and archive), AWS S3 Bucket (destination), AWS Lambda, AWS CloudWatch.

Step 1: Preparation --
Create and download a service account key from your Google Cloud Platform environment. The credentials are a key-value pair stored in JSON format. The steps are outlined at https://cloud.google.com/iam/docs/creating-managing-service-account-keys.

Step 2: Update the function code --
Download the connection.py function code and update with your bucket names and google credentials. There are four input variables that you need to fill.

Step 3: Create a zip folder --
In order to get Lambda to run your code, you have to package the contents in a zip folder containing 1) your source code, 2) google credentials, 3) google cloud client library. 
