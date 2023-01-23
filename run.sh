#!/bin/bash

# the name of the virtual environment
VENV_NAME='myenv'

# create virtual environment
python3 -m venv $VENV_NAME

# activate the virtual environment
source $VENV_NAME/bin/activate

# install the required modules
pip install -r requirements.txt

# the path of the main script
SCRIPT_PATH='main.py'

# execute the script
python3 $SCRIPT_PATH

# print a message indicating the script has finished
echo "Media files have been organized successfully."

# deactivate virtual environment
deactivate
