import boto3
import os

S3_BUCKET = os.getenv('S3_BUCKET')
S3_CLIENT = boto3.client('s3')

def download_files_from_s3(local_dir):
    '''
    Helper function to download files from S3 Bucket
    '''
    objects = S3_CLIENT.list_objects_v2(Bucket=S3_BUCKET)
    for obj in objects.get("Contents", []):
        file_name = obj["Key"]
        local_path = os.path.join(local_dir, file_name)
        S3_CLIENT.download_file(S3_BUCKET, file_name, local_path)
        print(f"Downloaded {file_name} to {local_path}")