import json

def lambda_handler(event, context):
    # TODO implement
    s = 'Hello World!!!'
    return {
        'statusCode': 200,
        'body': json.dumps(s)
    }
