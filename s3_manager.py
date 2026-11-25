# s3_manager.py
import boto3
from config import AWS_ACCESS_KEY, AWS_SECRET_KEY, AWS_REGION, AWS_ENDPOINT, BUCKET_NAME


class S3Manager:

    def __init__(self):

        self.s3 = boto3.client(
            "s3",
            endpoint_url=AWS_ENDPOINT,
            aws_access_key_id=AWS_ACCESS_KEY,
            aws_secret_access_key=AWS_SECRET_KEY,
            region_name=AWS_REGION,
        )

        self.bucket_name = BUCKET_NAME

    def create_bucket(self):
        try:

            self.s3.create_bucket(Bucket=self.bucket_name)

            print(f"Bucket '{self.bucket_name}' created successfully.")

        except self.s3.exceptions.BucketAlreadyOwnedByYou:

            print("Bucket already exists.")

        except Exception as e:

            print("Error creating bucket:", e)
