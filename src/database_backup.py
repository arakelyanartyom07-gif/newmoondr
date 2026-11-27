from ssm_runner import run_command


def create_dump(
    instance_id,
    db_secret,
    dump_path
):

    host = db_secret["database-host"]
    port = db_secret["database-port"]
    database = db_secret["database-name"]
    user = db_secret["database-user"]
    password = db_secret["database-password"]

    command = f"""
    export PGPASSWORD='{password}'

    pg_dump \
        -h {host} \
        -p {port} \
        -U {user} \
        -d {database} \
        -Fc \
        -f {dump_path}
    """

    return run_command(
        instance_id,
        [command],
        wait_seconds=15
    )