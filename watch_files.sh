#!/usr/bin/env bash

# -e exit if any command exits with a non zero code
# -u error out if there is an undefined variable
# -x show a command as it runs 
# -o pipefail if a command in a middle of a pipe fails the whole pipe fails
set -euxo pipefail

# echo "09" | xargs -t -I{} watchmedo shell-command -W --patterns='day{}.py;day{}_test.py' --recursive --command='pytest -v -s day{}/day{}_test.py' .
watchmedo shell-command -W --patterns='day'"$1"'.py;day'"$1"'_test.py' --recursive --command='pytest -v -s day'"$1"'/day'"$1"'_test.py' .
