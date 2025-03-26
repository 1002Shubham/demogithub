import boto3

client = boto3.client('s3')

response = client.put_bucket_versioning(
    Bucket='shubham-boto3-hcl',
    VersioningConfiguration={
        'Status': 'Enabled',
    },
)

print(response)
