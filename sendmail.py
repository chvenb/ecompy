import boto3
import tkinter as tk
from tkinter import messagebox
import random

def send_otp():
    

    aws_access_key_id1 = 'pppp'
    aws_secret_access_key1 = 'ppppp'
    region_name1 = 'ap-south-1'

    sns = boto3.client('sns', aws_access_key_id=aws_access_key_id1, aws_secret_access_key=aws_secret_access_key1, region_name=region_name1)

    # Specify your SNS topic name
    topic_name = 'ecompy_211'

    # Get or create the topic ARN
    response = sns.create_topic(Name=topic_name)
    topic_arn = response['TopicArn']

    otp = ''.join([str(random.randint(0, 9)) for _ in range(6)])

    # Your message with the OTP
    message = f'Your OTP is: {otp}'

    # Send an SMS
    response = sns.publish(
        TopicArn=topic_arn,
        Message=message,
        
    )

    print(f"Message ID: {response.get('MessageId')}")

    if response.get('MessageId'):
        print(f"OTP Sent: {otp}")
    else:
        print(f"Failed to send OTP. Response: {response}")

    


def send_report(num):

    

    aws_access_key_id1 = ''
    aws_secret_access_key1 = 'V'
    region_name1 = 'eu-north-1'

    sns = boto3.client('sns', aws_access_key_id=aws_access_key_id1, aws_secret_access_key=aws_secret_access_key1, region_name=region_name1)

    # Specify your SNS topic name
    topic_name = 'ecompy-211'

    # Get or create the topic ARN
    response = sns.create_topic(Name=topic_name)
    topic_arn = response['TopicArn']
    

    message = f"the following phone number {num} attempted unauthorised access"

    response = sns.publish(
        TopicArn=topic_arn,
        Message=message
    )

    print("reported")












