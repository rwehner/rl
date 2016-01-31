#!/usr/bin/env bash
# assumes Python3 with PyTest installed

# Get the testing dir based on location of this script
TEST_DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )/.." && pwd )

# Set up virtualenvwrapper, if present
if ( which virtualenvwrapper.sh 2>&1 > /dev/null ); then
    TARGET_VENV_NAME=codingbat-3
    if [ -n "${VIRTUAL_ENV}" -o "${VIRTUAL_ENV##*/}" != "${TARGET_VENV_NAME}" ]; then
       export VIRTUALENVWRAPPER_PYTHON=$(which python)
       export WORKON_HOME=~/virtualenv
       export PROJECT_HOME=~/projects
       export VIRTUALENVWRAPPER_HOOK_DIR=${WORKON_HOME}/hooks
       source $(which virtualenvwrapper.sh)
       workon "${TARGET_VENV_NAME}"
    fi
fi

# run the tests
python -m pytest "${TEST_DIR}"
