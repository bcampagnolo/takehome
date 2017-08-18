#!/bin/bash
set -euo pipefail
set -o posix
IFS=$'\n\t'

# Define a timestamp function
function timestamp {
  ts=$(date +"%Y-%m-%d-%h-%s")
  echo "$ts"
}

function do_zip {
  zip -r ../deploy/node/node_list_sha.zip *
  timestamp
}

function do_package {
aws --profile takehome cloudformation package \
   --template-file node_list_sha_package.yaml \
   --output-template-file node_list_sha_output.yaml \
   --s3-bucket artifacts-7135-2626-9054-us-west-2

timestamp

}

do_zip
do_package
