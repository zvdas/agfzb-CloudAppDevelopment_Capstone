from cloudant import Cloudant

def main(dict):
from cloudant.client import Cloudant

def main(dict):
    client = Cloudant.iam(account_name=dict['ACCOUNT_NAME'], api_key=dict['API_KEY'], connect=True)
    return {"reviews": [x for x in client['reviews']]}