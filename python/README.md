# My Python Project

This is a basic Python project scaffold. 

## Project Structure

The project has the following structure:

```
my-python-project
├── src
│   └── main.py
├── tests
│   └── test_main.py
├── .gitignore
├── setup.py
├── requirements.txt
└── README.md
```

## Description of Files

- `src/main.py`: This is the main Python script of the application. It contains the main logic of the application, including classes, functions, and execution code.

- `tests/test_main.py`: This is a test script for the main Python script. It contains various test cases and assertions to ensure the correct functionality of the main script.

- `.gitignore`: This file is used by Git to determine which files and directories to ignore when committing changes.

- `setup.py`: This is the build script for setuptools. It tells setuptools about your package (such as the name and version) as well as files to include.

- `requirements.txt`: This file lists all of the Python packages that your project depends on. You can specify the version number of each package as well.

## Installation

To install the dependencies of this project, run the following command:

```
pip install -r requirements.txt
```


## Setup Cloud Dependencies
We're using both Pinecone and OpenAI.  You will need to set up both and you need the following environment variables

```
OPENAI_API_KEY=<your key>
# Pinecone-client keys
PINECONE_ENV=gcp-starter
PINECODE_API_KEY=<your key>
```




## Usage

To run the main script of this project, navigate to the `src` directory and run the following command:

```
streamlit run python/scripts/exp_chatbot_app_sw.py
```

## Docker Setup

To run the docker container
```
docker compose up --build
```



## Testing

To run the tests for this project, navigate to the `tests` directory and run the following command:

```
python test_main.py
```

## Contributing

Contributions to this project are welcome. Please fork this repository, make your changes, and submit a pull request.