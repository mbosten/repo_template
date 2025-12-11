# Project Name


A template repository which can be used as a starting point for scientific analyses.


## Quickstart (Windows/macOS/Linux)

### 1. Set up the virtual environment
```bash
# 1) Create local env and install deps
uv venv --seed --python 3.12
uv sync --all-extras --group dev
```

### 2. Github integration
Either git clone this repository, use it as a template or copy the files and manually connect to your own repo as indicated below.
First create a repository in the Github web interface without readme, licence and gitignore. Then, run the following lines in the project root folder locally. 
```bash
git init
git remote add origin git@github.com/[username]/repo_template.git
git add .
git commit -m "Initial commit"
git push -u origin main
```

## Functionality
This repository contains several convenience functions such as logging, repository tree structure creation and command line integration. 

### 1. Logging
The file `src/newproject/logging_config.py` sets up a logger for both the console and a debug file. The output is structured to make the debug log easy to read by separating each running instance of the code and by color coding logger messages such that these are distinguisable. Feel free to change the color scheme to accomodate different use-cases such as for color blindness (which has not yet been integrated). 
The setup is required only in `cli.py`. In all other scripts, simply `import logging` and include `logger = logging.getLogger(__name__)` below your library imports. 
Subsequent logging is as easy as `logger.info("This prints to console and debug.log")` and `logger.debug("This only prints to debug.log")`.

### 2. Your Own Repository Tree
The file `src/newproject/readme_tree.py` creates a directory tree of your project based on the folder exclusions and file extension inclusions that are set in the script itself.
simply run `uv run src/newproject/readme_tree.py` from the project root and copy the output to your own `README.md` file.
```bash
        .-'- -.  
       (  ó    ) 
      (  ,    ó )
       ( './  .' 
        '-| |-'  
          | |
          |.|
PROJECT_TEMPLATE_GITHUB
-----------------------
├── data
│   ├── interim
│   ├── processed
│   └── raw
├── logs
├── src
│   └── newproject
│       ├── io
│       │   └── storage.py
│       ├── pipeline
│       ├── __init__.py
│       ├── cli.py
│       ├── logging_config.py
│       └── readme_tree.py
└── README.md
```

### 3. Command Line Integration
To simplify running the project this code base contains CLI functionality in `src/newproject/cli.py`. In this file we set up the logger and specify command line functions using the Typer module. Moreover, `pyproject.toml` builds this code base as a libary such that you can set your own CLI functions. Currently the `uv run np run-pipeline` is set to run `uv run src/newproject/cli.py:app run-pipeline`. The integration also circumvents having to set the Python executable directory manually from the CLI.
You can add your own commands that link to other CLI scripts as well.
