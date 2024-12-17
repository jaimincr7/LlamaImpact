import boto3
import os

S3_BUCKET = os.getenv('S3_BUCKET')
S3_PREFIX = os.getenv('S3_PREFIX')
S3_CLIENT = boto3.client('s3')

def upload_file_to_s3(directory):
    '''
    Helper function to upload file to S3 Bucket
    '''
    for file in os.listdir(directory):
        if file.endswith('.pdf'):
            S3_CLIENT.upload_file(
                os.path.join(directory, file), 
                S3_BUCKET, f'{S3_PREFIX}/{file}'
            )
            print(f"Uploaded {file} to {S3_BUCKET}")