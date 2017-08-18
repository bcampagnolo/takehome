#!/bin/bash
set -euo pipefail
set -o posix
IFS=$'\n\t'

# Define a timestamp function
function timestamp {
  ts=$(date +"%Y-%m-%d-%h-%s")
  echo "$ts"
}

timestamp
function do_deploy {
  aws --profile takehome cloudformation deploy \
    --template-file python_list_sha_output.yaml \
    --stack-name takehome-python-${ts} \
    --capabilities CAPABILITY_IAM

timestamp

}

do_deploy
