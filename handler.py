import boto3
from botocore.exceptions import ClientError
import json
import os
import time
import uuid
import decimal

client = boto3.client('ses', region_name=os.environ['SES_REGION'])
sender = os.environ['SENDER_EMAIL']
subject = os.environ['EMAIL_SUBJECT']
configset = os.environ['CONFIG_SET']
charset = 'UTF-8'

dynamodb = boto3.resource('dynamodb')

def sendMail(event, context):
    print(event)

    try:
        data = event['body']
        content = 'Sender Email: ' + data['email'] + ',<br> FullName: ' + data['fullname'] + ',<br> Form Type: ' + data['type'] + ',<br> Message Contents: ' + data['message']
        saveToDynamoDB(data)
        response = sendMailToUser(data, content)
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message Id:"),
        print(response['MessageId'])
    return "Email sent!"

def list(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    # fetch all records from database
    result = table.scan()

    #return response
    return {
        "statusCode": 200,
        "body": result['Items']
    }

def saveToDynamoDB(data):
    timestamp = int(time.time() * 1000)
    # Insert details into DynamoDB Table
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])
    item = {
        'id': str(uuid.uuid1()),
        'fullname': data['fullname'],
        'email': data['email'],
        'type': data['type'],
        'message': data['message'],
        'createdAt': timestamp,
        'updatedAt': timestamp
    }
    table.put_item(Item=item)
    return

def sendMailToUser(data, content):
    # Send Email using SES
    return client.send_email(
        Source=sender,
        Destination={
            'ToAddresses': [
                sender,
            ],
        },
        Message={
            'Subject': {
                'Charset': charset,
                'Data': subject
            },
            'Body': {
                'Html': {
                    'Charset': charset,
                    'Data': content
                }
            }
        }
    )
