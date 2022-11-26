# A.A. Jalbani @Dec 2022
# lambda function to convert audio to text.
# 1. IAM ROLE required (S3Bucket Full access, Cloud Watch full access, Transcribe) - if you are using AWS Academy, attach LABROLE
# 2. Create S3 bucket with attach event.
# 3. upload audio file
# Ref: https://towardsdatascience.com/a-quick-tutorial-to-aws-transcribe-with-python-53bbf6605a55 

import boto3
import uuid
import json

def lambda_handler(event, context):
    print(json.dumps(event))
    
    record = event["Records"][0]
    
    s3bucket = record["s3"]["bucket"]["name"]
    s3object = record["s3"]["object"]["key"]
    
    s3Path = f's3://{s3bucket}/{s3object}'
    jobName = f'{s3object}--{str(uuid.uuid4())}'
    outputKey = f'transcripts/{s3object}-transcript.json'
    
    client = boto3.client("transcribe")
    response = client.start_transcription_job(
        TranscriptionJobName = jobName,
        LanguageCode = 'en-US',
        Media = {"MediaFileUri":s3Path},
        OutputBucketName = s3bucket,
        OutputKey = outputKey
        )
        
    print(json.dumps(response,default=str))
    return {
        "TranscriptionJobName" : response['TranscriptionJob']['TranscriptionJobName']
    }
