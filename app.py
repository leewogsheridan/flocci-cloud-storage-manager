# app.py
from s3_manager import S3Manager


def main():

    storage = S3Manager()

    storage.create_bucket()


if __name__ == "__main__":

    main()
