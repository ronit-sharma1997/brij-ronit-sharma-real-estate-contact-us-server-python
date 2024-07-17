import boto3
import json

def lambda_handler(event, context):
    body = json.loads(event["body"])
    name = body.get('name')
    email = body.get('email')
    message = body.get('message')

    if name is None or email is None or message is None:
        return {
            "statusCode": 400,
            "body": json.dumps({
                "message": "Required body params missing: name, email, message"
            })
        }

    templateData = {
        "name": name,
        "email": email,
        "message": message
    }

    try:
        client = boto3.client('ses')
        response = client.send_templated_email(
            Source='ronit.sharma1997@gmail.com',
            Destination={
                'ToAddresses': [
                    'ronit.sharma1997@gmail.com',
                ]
            },
            Template='ExampleTemplate',
            TemplateData=json.dumps(templateData)
        )

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Email Sent"
            }),
        }
    except:
        return {
            "statusCode": 500,
            "body": json.dumps({
                "message": "Unable to send email",
            }),
        }
