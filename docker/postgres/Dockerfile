FROM postgres:15

RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates \
    && rm -rf /var/lib/apt/lists/*

RUN curl -fL "https://github.com/wal-g/wal-g/releases/download/v3.0.5/wal-g-pg-ubuntu-22.04-amd64" \
      -o /usr/local/bin/wal-g \
    && chmod +x /usr/local/bin/wal-g \
    && wal-g --version

RUN mkdir -p /var/lib/postgresql/backups