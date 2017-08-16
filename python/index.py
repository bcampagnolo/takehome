import json
import logging
import requests
import pyjq
from jq import jq
from pprint import pprint


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

with open('./data/commits.json') as data_file:
    data = json.load(data_file)
    pyjq.all()
pprint(data)


url = 'https://api.github.com/repos/stedolan/jq/commits?per_page=50'

params = dict(
    Headers='User-Agent: request'
)

response = requests.get(url=url, params=params)
data = response.json(jq '.[] | select(.commit.author.name == .commit.committer.name) | .sha')

jq '.[] | select(.commit.author.name == .commit.committer.name) | .sha'

print (data)
