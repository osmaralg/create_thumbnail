import json
from PIL import Image
def lambda_handler(event, context):
    # TODO implement

    val_1 = event["queryStringParameters"]['min']
    val_2 = event["queryStringParameters"]['max']
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!' + str(int(val_1)*int(val_2)))
    }