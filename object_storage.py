import boto3
import logging
from botocore.exceptions import ClientError
from config import s3_config


def put_object(photo, unique_id):

    try:
        object_name = f'{unique_id}.jpg'

        bucket.put_object(
            Body=photo,
            ACL='public-read',
            Key=object_name,
        )
        print(">>> uploading object Done ^^")
    except ClientError as e:
        logging.error(e)


def get_object(object_name):

    try:
        object_name = f'{object_name}.jpg'
        download_path = f'photos\{object_name}'

        bucket.download_file(
            object_name,
            download_path
        )
        print(">>> Downloading object Done ^^")
        
    except ClientError as e:
        logging.error(e)
  
  
def get_object_url(object_name):
    return f'https://s3.ir-thr-at1.arvanstorage.com/adsphoto/{object_name}.jpg'
        
            
try:
    s3_resource = boto3.resource(
        's3',
        endpoint_url=s3_config["endpoint_url"],
        aws_access_key_id=s3_config['aws_access_key_id'],
        aws_secret_access_key=s3_config['aws_secret_access_key']
    )

except Exception as exc:
    logging.error(exc)

bucket = s3_resource.Bucket('adsphoto')
    
        