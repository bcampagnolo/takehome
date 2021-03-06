# takehome
Sample work to explore building and deploying lambda functions.

# Approach
GitHub has a JSON API, so lets explore using the API. The following URL gets us the last commits from the `jq`
repo.
https://api.github.com/repos/stedolan/jq/commits

* bash/perl/go/python/scripting parsing exercise:
Write a script to grab the last 50 commits and extract a list of the hashes/SHA for commits that
have a different author than commitor.
* programming exercise:
Convert the above script into an AWS lambda compatible language function.
* application deployment exercise:
Provide the cloudformation template, or scripts, used to deploy the above lambda function into
AWS and show sample execution

# Prerequisites
Ensure the amazon cli tools are installed and configuration is complete. The build and deploy scripts expect a profile of `takehome` to be set.

## Usage
the `python` and `node` folders each have a `deploy.sh` and `package.sh` Package will update the cf template and prepare things for upload to S3 and deploy will do the work.
Alternatively, the node sample can be done in a single step `npm run deploy`. This requires node and npm to be installed, and the intent would be to have a Jenkins or Travis job call the npm script.

## CodeStar
AWS Code star may also be used - that work is located here:

# Current API GW URL

* [node GET url](https://vai4prg0r7.execute-api.us-west-2.amazonaws.com/prod/ "node GET")
* [python GET url](https://52ion0v16i.execute-api.us-west-2.amazonaws.com/Prod/python_list_sha/ "python GET")
