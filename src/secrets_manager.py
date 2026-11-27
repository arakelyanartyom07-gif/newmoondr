import json
import boto3


def get_secret(secret_name: str) -> dict:

    client = boto3.client(
        "secretsmanager",
        region_name="eu-central-1"
    )

    response = client.get_secret_value(
        SecretId=secret_name
    )

    return json.loads(
        response["SecretString"]
    )