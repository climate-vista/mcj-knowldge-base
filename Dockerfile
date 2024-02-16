# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.12.1-slim

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY python/requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY . /app

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app


# Build up the pip requirements and streamlit requirements
RUN python -m pip install --upgrade pip
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*


# Download dependencies as a separate step to take advantage of Docker's caching.
# Leverage a cache mount to /root/.cache/pip to speed up subsequent builds.
# Leverage a bind mount to requirements.txt to avoid having to copy them into
# into this layer.
RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=./python/requirements.txt,target=./python/requirements.txt \
    python -m pip install -r ./python/requirements.txt


#Environment variables for the chatbot
# Don't put API keys here

# Pinecone-client keys
ENV PINECONE_ENV=gcp-starter 


ENV HOST=0.0.0.0
ENV LISTEN_PORT 8080
# Expose the port that the application listens on.
EXPOSE 8080
HEALTHCHECK CMD curl --fail http://localhost:8080/_stcore/health


USER appuser



# Run the application.
ENTRYPOINT ["streamlit", "run", "/app/python/scripts/exp_chatbot_app_sw.py", "--server.port=8080"]

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
#CMD ["python", "python\scripts\exp_chatbot_app_sw.py"]
