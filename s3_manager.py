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

    def upload_file(self, file_path, object_name=None):

        try:

            if object_name is None:

                object_name = file_path.split("/")[-1]

            self.s3.upload_file(file_path, self.bucket_name, object_name)

            print(f"File uploaded successfully: {object_name}")

        except Exception as e:

            print("Upload failed:", e)

    def list_files(self):

        try:

            response = self.s3.list_objects_v2(Bucket=self.bucket_name)

            if "Contents" not in response:

                print("Bucket is empty.")

                return

            print("\nFiles stored in S3:\n")

            for obj in response["Contents"]:

                print(f"File: {obj['Key']} | " f"Size: {obj['Size']} bytes")

        except Exception as e:

            print("Error listing files:", e)

    def download_file(self, object_name, download_path):

        try:

            self.s3.download_file(self.bucket_name, object_name, download_path)

            print(f"Downloaded successfully: {download_path}")

        except Exception as e:

            print("Download failed:", e)

    def delete_file(self, object_name):

        try:

            self.s3.delete_object(Bucket=self.bucket_name, Key=object_name)

            print(f"Deleted successfully: {object_name}")

        except Exception as e:

            print("Delete failed:", e)

    def file_information(self, object_name):

        try:

            response = self.s3.head_object(Bucket=self.bucket_name, Key=object_name)

            print("\nFile Information")

            print("----------------------")

            print("Name:", object_name)

            print("Size:", response["ContentLength"], "bytes")

            print("Content Type:", response.get("ContentType"))

            print("Last Modified:", response["LastModified"])

        except Exception as e:

            print("Unable to retrieve file information:", e)
