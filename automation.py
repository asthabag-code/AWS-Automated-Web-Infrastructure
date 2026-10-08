import boto3

region = "ap-south-1"

ec2 = boto3.client("ec2", region_name=region)

response = ec2.describe_instances()

print("AWS connection successful!")
print("EC2 reservations:", len(response["Reservations"]))