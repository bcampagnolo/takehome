#!/bin/bash
set -euo pipefail
set -o posix
IFS=$'\n\t'

# Define a timestamp function
function timestamp {
  ts=$(date +"%Y-%m-%d-%h-%s")
  echo "$ts"
}

function get_requirements {
  REQS=( `cat requirements.txt` )
  for REQ in "${REQS[@]}"; do
    pip install -t . ${REQ}
    timestamp
  done;
}

function do_zip {
  mkdir -p ../deploy/python/
  zip -r ../deploy/python/python_list_sha.zip *
  timestamp
}

timestamp
function do_package {
  aws --profile takehome cloudformation package \
  --template-file python_list_sha_package.yaml \
  --output-template-file python_list_sha_output.yaml \
  --s3-bucket artifacts-7135-2626-9054-us-west-2

  timestamp

}

get_requirements
do_zip
do_package
