#!/bin/bash
# Script should be run from the root of the repository.

set -e

use_color=true

# Colors for printing pass/fail
if [ "${use_color}" = true ]; then
  error_color='\033[0;31m'
  pass_color='\033[0;32m'
  no_color='\033[0m'
else
  error_color=""
  pass_color=""
  no_color=""
fi

pylint_directories=( src/ )

errors=0

. .venv/bin/activate
echo "--- Running pylint"
pylint ${pylint_directories[@]} || ((errors=errors+1))
deactivate

if [ ${errors} -gt 0 ]; then
  echo -e "\n--- ${error_color}${errors} TESTS FAILED, please correct the"\
    "above errors${no_color}"
  exit 1
else
  echo -e "\n--- ${pass_color}ALL TESTS PASSED${no_color}"
fi