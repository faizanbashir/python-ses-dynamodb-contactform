import boto3
from botocore.exceptions import ClientError
import os

client = boto3.client('ses')
sender = 'faizan.ibn.bashir@gmail.com'
subject = 'Serverless Mail'
configset = 'ConfigSet'
charset = 'UTF-8'

def sendMail(event, context):
    # Print event
    print(event)

    try:
        firstname = event['body']['firstname']
        lastname = event['body']['lastname']
        recipient = event['body']['email']
        message = event['body']['message']
        content = 'Message from ' + firstname + ' ' + lastname + ', sez: ' + message

        response = client.send_email(
            Source=sender,
            Destination={
                'ToAddresses': [
                    recipient,
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
                    },
                    'Text': {
                        'Charset': charset,
                        'Data': content
                    }
                }
            }
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message Id:"),
        print(response['MessageId'])
    return "Email sent!"
