import boto3

s3_client = boto3.client("s3")


# client = boto3.client('rds')
def lambda_handler(event, context):
    # s3 bucket name
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    s3_client_name =  event['Records'][0]['s3']['object']['key']
    response = s3_client.get_object(Bucket=bucket_name,Key=s3_client_name)
    ## data
    data = response['Body'].read()

    # # printing the data
    # print(data)

    ## add the data into the RDS




