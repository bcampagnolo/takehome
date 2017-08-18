import json
import logging
from ratelimit import rate_limited
import requests
import pyjq
from apierror import apierror

# All commit info we care about for exercise #
# .[] | {author: .commit.author.name, name: .commit.committer.name, sha: .sha}'
#
# Filtered commit info
# .[] | select(.commit.author.name == .commit.committer.name) | .sha
url = 'https://api.github.com/repos/stedolan/jq/commits?per_page=50'

# --- Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

handler = logging.FileHandler('./logs/python.log')
handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(handler)
logger.info('Starting application')
# --- END of Logging

def parse_data():
    if test
with open('./data/commits.json') as data_file:
    data = json.load(data_file)
    filtered = pyjq.all('.[] | {author: .commit.author.name, name: .commit.committer.name, sha: .sha}', data)

print json.dumps(filtered, indent=2)

@rate_limited(1)
def call_api(self, url):
  response = requests.get(url)
  logger.info('Connecting to API URL', self.url())
  if response.status_code != 200:
    raise apierror('Cannot call API: {}'.format(response.status_code))

  return response

# url = 'https://api.github.com/repos/stedolan/jq/commits?per_page=50'
#
# params = dict(
#     Headers='User-Agent: request'
# )
#
# response = requests.get(url=url, params=params)
# data = response.json(jq '.[] | select(.commit.author.name == .commit.committer.name) | .sha')
#
# jq '.[] | select(.commit.author.name == .commit.committer.name) | .sha'
#
# print (data)
