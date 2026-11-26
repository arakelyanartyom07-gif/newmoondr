import time

from jobs_loader import load_jobs
from rclone_runner import sync_bucket


def run():

    config = load_jobs()

    for env in config["environments"]:

        try:

            bucket = env.get("bucket")

            if bucket:

                print(
                    f"Synchronizing {env['name']}"
                )

                sync_bucket(
                    bucket["source"],
                    bucket["destination"]
                )

        except Exception as exc:

            print(exc)


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