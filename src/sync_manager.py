import time

from jobs_loader import load_jobs
from rclone_runner import sync_bucket


def run():

    config = load_jobs()

    for bucket in config["buckets"]:

        try:

            print(
                f"Synchronizing {bucket}"
            )

            sync_bucket(bucket)

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