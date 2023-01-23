#!/bin/bash

VENV_NAME='myenv'

# create virtual environment
python3 -m venv $VENV_NAME

# activate the virtual environment
source $VENV_NAME/bin/activate

pip install -r requirements.txt

SCRIPT_PATH='main.py'

python3 $SCRIPT_PATH

echo "Media files have been organized successfully."

# deactivate virtual environment
deactivate
