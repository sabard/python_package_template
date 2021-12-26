#!/bin/sh
set -v

pyenv activate [[package_name]]

pip install --upgrade setuptools pip
pip install wheel pip-tools

pip-compile "$@"
pip-sync requirements.txt
