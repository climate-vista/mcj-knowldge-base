# My Python Project

This is a basic Python project scaffold. 

## Project Structure

The project has the following structure:

```
my-python-project
├── scripts
│   └── 
├── tests
│   └── test_main.py
├── .gitignore
├── .env
├── setup.py
├── requirements.txt
└── README.md
```

## Description of Files

- `scripts/exp_chatbot_app_sw.py`: This is the main script for the application that should be run from streamlit. 

- `.gitignore`: This file is used by Git to determine which files and directories to ignore when committing changes.

- `.env`: Environment file for setting custom environment variables for your python app.  

- `setup.py`: This is the build script for setuptools. It tells setuptools about your package (such as the name and version) as well as files to include.

- `requirements.txt`: This file lists all of the Python packages that your project depends on. You can specify the version number of each package as well.

## Installation

Setup a local environment
```
python -m venv <localpath>
```

To install the dependencies of this project, run the following command:

```
pip install -r requirements.txt
```

Create a local environment variable file .env and set the following variables
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

## Testing

There are currently no tests for this repo

## Contributing

Contributions to this project are welcome. Please fork this repository, make your changes, and submit a pull request.