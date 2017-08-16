import json
import requests
from jq import jq
from pprint import pprint

with open('./commits.json') as data_file:
    data = json.load(data_file)

pprint(data)

#
# url = 'https://api.github.com/repos/stedolan/jq/commits?per_page=50'
#
# params = dict(
#     Headers='User-Agent: request'
# )
#
# response = requests.get(url=url, params=params)
# # data = response.json(jq '.[] | select(.commit.author.name == .commit.committer.name) | .sha')
#
# # jq '.[] | select(.commit.author.name == .commit.committer.name) | .sha'
#
# print (data)
