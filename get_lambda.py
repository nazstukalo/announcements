import json
import boto3

dynamodb = boto3.resource('dynamodb')
announcements_table = dynamodb.Table('tabmine')

def lambda_handler(event, context):
  response = announcements_table.scan()
  return {
    'statusCode': 200,
    'body': response['Items']
  }