import time

from jobs_loader import load_jobs
from secrets_manager import get_secret
from rclone_runner import sync_bucket


def run():

    config = load_jobs()

    for env in config["environments"]:

        try:

            print(
                f"Processing environment: {env['name']}"
            )

            rclone_secret = get_secret(
                env["rclone_secret"]
            )

            db_secret = get_secret(
                env["db_secret"]
            )

            print(
                "Secrets loaded successfully"
            )

            bucket = env.get(
                "bucket"
            )

            if bucket:

                print(
                    f"Synchronizing {env['name']} bucket"
                )

                sync_bucket(
                    bucket["source"],
                    bucket["destination"]
                )

            print(
                f"Environment {env['name']} completed"
            )

        except Exception as exc:

            print(
                f"{env['name']} : {exc}"
            )


if __name__ == "__main__":

    config = load_jobs()

    interval = config["interval_hours"]

    while True:

        print(
            "Starting sync cycle"
        )

        run()

        print(
            f"Sleeping for {interval} hours"
        )

        time.sleep(
            interval * 3600
        )