import json
import boto3

#some text
dynamodb = boto3.resource('dynamodb')
announcements_table = dynamodb.Table('tabmine')

def lambda_handler(event, content):
    announcements_table.put_item(Item=event['queryStringParameters'])
    return {
        'statusCode': 200,
        'body': json.dumps('Added Entry Successfully!')
    }