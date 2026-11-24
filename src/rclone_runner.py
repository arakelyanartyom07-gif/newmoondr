import subprocess


def bucket_exists(remote, bucket):
    result = subprocess.run(
        [
            "rclone",
            "lsd",
            f"{remote}:"
        ],
        capture_output=True,
        text=True
    )

    return bucket in result.stdout


def create_bucket(remote, bucket):
    subprocess.run(
        [
            "rclone",
            "mkdir",
            f"{remote}:{bucket}"
        ],
        check=False
    )


def sync_bucket(bucket):

    source = f"aws3:{bucket}"
    destination = f"rustfs:{bucket}"

    if not bucket_exists("rustfs", bucket):
        create_bucket("rustfs", bucket)

    subprocess.run(
        [
            "rclone",
            "sync",
            source,
            destination,
            "--progress",
            "--create-empty-src-dirs"
        ],
        check=False
    )