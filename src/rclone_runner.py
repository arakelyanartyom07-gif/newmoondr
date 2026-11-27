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
        check=True
    )


def sync_bucket(source, destination):

    bucket_name = destination.split(":")[1]

    if not bucket_exists("rustfs", bucket_name):
        create_bucket("rustfs", bucket_name)

    subprocess.run(
        [
            "rclone",
            "sync",
            source,
            destination,
            "--progress",
            "--create-empty-src-dirs"
        ],
        check=True
    )