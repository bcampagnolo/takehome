import json
import requests
import pyjq


# All commit info we care about for exercise #
# .[] | {author: .commit.author.name, name: .commit.committer.name, sha: .sha}'
#
# Filtered commit info
# .[] | select(.commit.author.name == .commit.committer.name) | .sha
# url = 'https://api.github.com/repos/stedolan/jq/commits?per_page=50'

isTest = False

def readFile():
    with open('./data/commits.json') as data_file:
        data = json.load(data_file)
        filtered = pyjq.all('.[] | select(.commit.author.name == .commit.committer.name) | .sha', data)

    print json.dumps(filtered, indent=2)
    return {'statusCode': 200,
            'body': json.dumps(filtered),
            'headers': {'Content-Type': 'application/json'}}

def readURL():
    url = 'https://api.github.com/repos/stedolan/jq/commits?per_page=50'

    params = dict(
        Headers='User-Agent: request'
    )

    response = requests.get(url=url, params=params)
    data = response.json()
    shas = pyjq.all('.[] | select(.commit.author.name == .commit.committer.name) | .sha', data)

    print json.dumps(shas, indent=2)
    return {'statusCode': 200,
            'body': json.dumps(shas),
            'headers': {'Content-Type': 'application/json'}}


def handler(event, context):
    if isTest == "True":
        readFile()
    else:
        readURL()

