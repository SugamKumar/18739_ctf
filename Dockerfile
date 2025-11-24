# Pinned Ubuntu 24.04 base image for deterministic builds
FROM ubuntu@sha256:e3f92abc0967a6c19d0dfa2d55838833e947b9d74edbcb0113e48535ad4be12a AS challenge

# Minimal runtime: Python for the encrypt script
RUN apt-get update && \
    apt-get install -y --no-install-recommends python3 && \
    rm -rf /var/lib/apt/lists/*

# cmgr expects /challenge for metadata and packaged artifacts
RUN mkdir -p /challenge /app && \
    chmod 700 /challenge

# Copy flag and encryption script into the image
# encrypt.py should read flag.txt and write cipher.txt in /app
COPY flag.txt encrypt.py /app/
WORKDIR /app

# Generate ciphertext, package artifacts for download, and record flag metadata
RUN python3 encrypt.py && \
    tar czvf /challenge/artifacts.tar.gz cipher.txt && \
    echo "{\"flag\":\"$(cat flag.txt)\"}" > /challenge/metadata.json

# Keep the container alive so cmgr can attach to it
CMD ["tail", "-f", "/dev/null"]
