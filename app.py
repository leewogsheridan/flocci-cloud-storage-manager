# app.py
from s3_manager import S3Manager


def main():

    storage = S3Manager()

    storage.create_bucket()

    storage.upload_file("uploads/sample.txt", "documents/sample.txt")

    storage.list_files()

    storage.download_file("documents/sample.txt", "downloads/sample_downloaded.txt")

    storage.delete_file("documents/sample.txt")


if __name__ == "__main__":

    main()
