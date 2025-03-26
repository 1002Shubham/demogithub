import boto3

client = boto3.client('s3')

response = client.put_bucket_encryption(
    Bucket='shubham-boto3-hcl',
    ServerSideEncryptionConfiguration={
        'Rules' : [
          {
                'ApplyServerSideEncryptionByDefault': {
                    'SSEAlgorithm': 'AES256',
                },
         },
    },
)

print(response)
