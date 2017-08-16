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
function do_package {
aws --profile takehome cloudformation package \
   --template-file example.yaml \
   --output-template-file serverless-output.yaml \
   --s3-bucket artifacts-7135-2626-9054-us-west-2

timestamp

}

do_package
