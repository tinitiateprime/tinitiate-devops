import json


def lambda_handler(event, context):
    print("Received event:")
    print(json.dumps(event))

    bucket = event.get("bucket", "not-provided")
    key = event.get("key", "not-provided")

    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": "File validation event received",
                "bucket": bucket,
                "key": key,
            }
        ),
    }
