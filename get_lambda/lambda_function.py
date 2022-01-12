import json
import boto3
#test
dynamodb = boto3.resource('dynamodb')
announcements_table = dynamodb.Table('tabmine')

def lambda_handler(event, context):
  response = announcements_table.scan()
  return {
    'statusCode': 200,
    'body': json.dumps(response['Items'])
  }