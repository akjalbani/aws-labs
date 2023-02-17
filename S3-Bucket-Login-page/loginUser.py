import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Users')

def lambda_handler(event, context):
    username = event['username']
    password = event['password']
    
    response = table.get_item(
        Key={
            'Username': username
        }
    )
    
    if 'Item' not in response:
        return {
            'statusCode': 404,
            'body': 'User not found'
        }
    
   
