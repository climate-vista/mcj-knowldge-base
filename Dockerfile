# syntax=docker/dockerfile:1

# Comments are provided throughout this file to help you get started.
# If you need more help, visit the Dockerfile reference guide at
# https://docs.docker.com/engine/reference/builder/

ARG PYTHON_VERSION=3.12.1
FROM python:${PYTHON_VERSION}-slim as base

# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Create a non-privileged user that the app will run under.
# See https://docs.docker.com/go/dockerfile-user-best-practices/
ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser


RUN python -m pip install --upgrade pip

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/streamlit/streamlit-example.git .

# Download dependencies as a separate step to take advantage of Docker's caching.
# Leverage a cache mount to /root/.cache/pip to speed up subsequent builds.
# Leverage a bind mount to requirements.txt to avoid having to copy them into
# into this layer.
RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=./python/requirements.txt,target=./python/requirements.txt \
    python -m pip install -r ./python/requirements.txt


#Environment variables for the chat
# Todo: Figure out how to hide these keys better

# Pinecone-client keys
ENV PINECONE_ENV=gcp-starter 

# API-KEYs needed
# You will need to set two environment variables at runtime
# PINECONE_API_KEY=xxxx - get key from pinecone.io
# OPENAI_API_KEY=xxxxx - get from openai

#Parameters for the script
ENV MCJ_TRANSCRIPT_DIR=./test-transcripts

#enable unbuffered python output for docker and streamlit
ENV PYTHONUNBUFFERED="Debug"

ENV HOST=0.0.0.0
ENV LISTEN_PORT 8080
# Expose the port that the application listens on.
EXPOSE 8080
HEALTHCHECK CMD curl --fail http://localhost:8080/_stcore/health

# Switch to the non-privileged user to run the application.
USER appuser

# Copy the source code into the container.
COPY . .



# Run the application.
ENTRYPOINT ["streamlit", "run", "/app/python/scripts/exp_chatbot_app_sw.py", "--server.port=8080"]
#ENTRYPOINT ["streamlit", "run", "streamlit_app.py", "--server.port=8080"] - this worked
#CMD gunicorn '.venv.Lib.site-packages.httpx._transports.wsgi' --bind=0.0.0.0:8000
