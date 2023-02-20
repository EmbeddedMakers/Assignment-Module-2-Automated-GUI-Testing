#!/usr/bin/env bash
# Script should be run from the root of the repository.

set -e
set -o nounset

pytest_directories=( tests/ )

rm -rf ./.venv

python3.8 -m venv .venv
. .venv/bin/activate
pip install --upgrade pip
pip install pytest pylint selenium webdriver-manager

deactivate
