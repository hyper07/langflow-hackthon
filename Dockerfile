FROM python:3.12-slim

# For Mac users: ensure Docker Desktop has file sharing enabled for your project directory.
RUN apt-get update && apt-get install -y gcc g++ git make \
    && rm -rf /var/lib/apt/lists/*
RUN useradd -m -u 1000 user
USER user
ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH

WORKDIR $HOME/app

COPY --chown=user . $HOME/app

# Ensure pip cache is not stored to reduce image size
RUN pip install --no-cache-dir "langflow>=0.0.71" -U --user
CMD ["langflow", "--host", "0.0.0.0", "--port", "7860"]
