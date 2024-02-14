# mcj-knowldge-base
Open collaboration project for knowledge discovery with My Climate Journey podcast


## Requirements - Pinecone.io and OPenAI API keys. 
Create and Set Your Environment Variables

Create a .env file locally
Set the following environment variables

PINECONE_API_KEY - from Pinecone.io
OPENAI_API_KEY - from OpenAI

These should NOT be checked in.


## Pull and Run Docker image
The public docker image is jrenouard/mcjknowldgebase

`docker pull jrenouard/mcjknowldgebase will pull that locally`

To run it you will need to add the port mapping and environment variables
E.g. from the command line
Set your environment variables in a .env file.
`docker run --rm -it --env-file ./.env -p 8080:8080/tcp jrenouard/mcjknowldgebase:latest`

Alternatively, set them explicitly on the docker command line.
`docker run --rm -it --env PINECONE_API_KEY=yyyyyy --env OPENAI_API_KEY=xxxxxx -p 8080:8080/tcp jrenouard/mcjknowldgebase:latest`

From Docker Desktop - make sure and set 8080 as the host port and set the environment variables in the run dialog.

The MCJ Bot should be running now in http://localhost:8080 


## Setup for building app and Docker container

### Local Python Environment
It is recommended that you setup a local python environments to keep the python libraries localized to the project.  

Command line: `python -m venv <localpath>`

VS Code you can Ctrl-Shift-P > Python: Create Environment.
Select Venv, your interpreter, etc.

This will create a .venv and all your packages will be downloaded into this local environment.



### Build Docker image
Install Docker Desktop

In VSCode, select the Dockerfile and "build docker image"

The Dockerfile is setup to run a streamlit environment in the container. It is also set to run the streamlit on port 8080. 







