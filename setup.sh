#!/bin/sh

eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

pyenv install 3.8.12 -s
pyenv virtualenv 3.8.12 python_package_template
./update-deps.sh
