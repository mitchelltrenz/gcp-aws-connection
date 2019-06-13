#import necessary packages
import json
from google.cloud import storage
import boto3
import io
#call the function
def lambda_handler(event, context):
    client = storage.Client.from_service_account_json('*')
    s3 = boto3.client("s3")
    gcp_bucket = '**'
    gcp_archive_bucket = '***'
    aws_bucket = '****'
    bucket = client.get_bucket(gcp_bucket)
    bucket2 = client.get_bucket(gcp_archive_bucket)
    blobs = bucket.list_blobs()
    for blob in blobs:
        with io.BytesIO() as data:
            blob.download_to_file(data)
            data.seek(0)
            s3.upload_fileobj(data, aws_bucket, blob.name)
            bucket.copy_blob(blob, bucket2, blob.name)
            blob.delete()

# * Insert Google Credentials (JSON format)
# ** Insert name of Google Bucket with CSV contents
# *** Insert name of Archived Google Bucket to house processed CSV contents
# **** Insert name of AWS S3 destination bucket
