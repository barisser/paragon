import boto
from boto.s3.connection import S3Connection
import os

access_key = os.environ['AWS_ACCESS_KEY']
secret_access_key = os.environ['AWS_SECRET_ACCESS_KEY']
DEFAULT_BUCKET = os.environ['PARAGON_BUCKET']

def upload(identifier, contents, bucket=DEFAULT_BUCKET):
    conn = S3Connection(access_key, secret_access_key)
    bucket = conn.get_bucket(bucket)
    key = boto.s3.key.Key(bucket)
    key.key = identifier
    key.set_contents_from_string(contents)
    bucket.set_acl('public-read', key)
    return key.generate_url(expires_in=0, query_auth=False)
