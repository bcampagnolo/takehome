import json
import requests
from pydash import py_

isTest = False


def readfile():
    with open('./data/commits.json') as data_file:
        data = json.load(data_file)

        filtered = py_.filter(data, {'commit.author.name' == 'commit.committer.name'})
        shas = py_.map_(filtered, '.sha')

    print(json.dumps(shas, indent=2))
    return {'statusCode': 200,
            'body': json.dumps(shas),
            'headers': {'Content-Type': 'application/json'}}


def readurl():
    url = 'https://api.github.com/repos/stedolan/jq/commits?per_page=50'

    params = dict(
        Headers='User-Agent: request'
    )

    response = requests.get(url=url, params=params)
    data = response.json()

    filtered = py_.filter(data, {'commit.author.name' == 'commit.committer.name'})
    shas = py_.map_(filtered, '.sha')

    print(json.dumps(shas, indent=2))
    return {'statusCode': 200,
            'body': json.dumps(shas),
            'headers': {'Content-Type': 'application/json'}}


def handler(event, context):
    if isTest == "True":
        readfile()
    else:
        readurl()

# def main():
#     if isTest == "True":
#         readfile()
#     else:
#         readurl()
#
# main()
