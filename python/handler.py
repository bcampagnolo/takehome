import json
import requests
from pydash import py_


def handler(event, context):
    url = 'https://api.github.com/repos/stedolan/jq/commits?per_page=50'

    params = dict(
        Headers='User-Agent: request'
    )

    response = requests.get(url=url, params=params)
    data = response.json()

    filtered = py_.filter(data, {'commit.author.name' == 'commit.committer.name'})
    shas = py_.map_(filtered, '.sha')

    # print(json.dumps(shas, indent=2))
    return {'statusCode': 200,
            'body': json.dumps(shas),
            'headers': {'Content-Type': 'application/json'}}
