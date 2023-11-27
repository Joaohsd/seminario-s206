#!/bin/bash

# Installing python module in order to create new python environment
pip install virtualenv

# Creating new environment based on argument passed to this script
python3 -m virtualenv venv

# Activate the Virtual Environment
source venv/bin/activate

# Install required dependencies for this Environment
pip install -r setup/requirements.txt

# Saving info about versions of installed packages
pip freeze > setup/packages.txt