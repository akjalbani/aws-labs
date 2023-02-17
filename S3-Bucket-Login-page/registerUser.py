import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Users')

def lambda_handler(event, context):
    username = event['username']
    password = event['password']
    first_name = event['first_name']
    last_name = event['last_name']
    address = event['address']
    
    table.put_item(
        Item={
            'Username': username,
            'Password': password,
            'First name': first_name,
            'Last name': last_name,
            'Address': address
        }
    )
    
    return {
        'statusCode': 200,
        'body': 'User registered successfully'
    }
