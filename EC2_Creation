import boto3

client = boto3.client('ec2')

response = client.run_instances(
   ImageId='ami-00bb6a80f01f03502',
   InstanceType='t2.micro',
   MaxCount = 1,
   MinCount = 1
)

print(response)

instance_details = client.describe_instances()

print(instance_details)
