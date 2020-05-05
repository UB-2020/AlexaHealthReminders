import json
import boto3
import os
from boto3 import client as boto3_client
from datetime import datetime


s3 = boto3.client('s3')
ddb = boto3.resource('dynamodb')
table = ddb.Table('patient')

def lambda_handler(event, context)
    response = table.scan()
    body = json.dumps(response['Items'])
    # print(body)
    #response = s3.put_object(Bucket='alexa-patient-bucket', Key='alexa-patient.json', Body=body, ContentType='applicationjson')
    # print(response)
    # # print('Items are...')
    # r=response['Items']
    # # print(r)
    # # print(type(r))
    # json_list = json.dumps(r)
    # print(json_list)
    
    lambda_client = boto3_client('lambda')

    msg = body
    invoke_response = lambda_client.invoke(FunctionName=arnawslambdaus-east-2563672427745functionalexa_skill,
                                           InvocationType='RequestResponse',
                                           Payload=msg
                                           )
    print('Calling...')                                       
    # print(invoke_response['Payload'].read().decode())
    print(invoke_response)