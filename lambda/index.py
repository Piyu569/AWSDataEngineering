import json
import datetime

def handler(event, context):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    print(f"Lambda function triggered at: {current_time}")
    
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': f'Lambda function executed successfully at {current_time}',
            'event': event
        })
    } 