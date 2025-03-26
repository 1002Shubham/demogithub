import boto3

s3_bucket = boto3.client('s3')

response = s3_bucket.create_bucket(
    Bucket = 'shubham-boto3-hcl'
  )

print(response)

