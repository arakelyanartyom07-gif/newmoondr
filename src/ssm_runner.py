import time

import boto3


REGION = "eu-central-1"


def send_command(
    instance_id: str,
    commands: list[str]
) -> str:

    ssm = boto3.client(
        "ssm",
        region_name=REGION
    )

    response = ssm.send_command(
        InstanceIds=[
            instance_id
        ],
        DocumentName="AWS-RunShellScript",
        Parameters={
            "commands": commands
        }
    )

    return response["Command"]["CommandId"]


def get_command_result(
    instance_id: str,
    command_id: str
) -> dict:

    ssm = boto3.client(
        "ssm",
        region_name=REGION
    )

    return ssm.get_command_invocation(
        CommandId=command_id,
        InstanceId=instance_id
    )


def run_command(
    instance_id,
    commands
):

    command_id = send_command(
        instance_id,
        commands
    )

    while True:

        result = get_command_result(
            instance_id,
            command_id
        )

        if result["Status"] in [
            "Success",
            "Failed",
            "TimedOut",
            "Cancelled"
        ]:
            return result

        time.sleep(2)