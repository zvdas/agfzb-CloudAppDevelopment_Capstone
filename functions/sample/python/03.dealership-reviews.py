# python 3.9
from ibmcloudant.cloudant_v1 import CloudantV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

def main(dict):
    authenticator = IAMAuthenticator(dict['API_KEY'])
    service = CloudantV1(authenticator=authenticator)
    service.set_service_url(dict['COUCH_URL'])
    response = service.post_find(db='reviews', selector={'dealership':{'$eq':dict['DEALERSHIP']}}).get_result()
    return response


# python 3.7
# from cloudant import Cloudant
from cloudant.client import Cloudant

def main(dict):
    client = Cloudant.iam(account_name=dict['ACCOUNT_NAME'], api_key=dict['API_KEY'], connect=True)
    
    selector = {'dealership': {'$eq': dict['DEALERSHIP']}}
    return {"dealership_reviews": [x for x in client['reviews'].get_query_result(selector)]}

/*
{
    "ACCOUNT_NAME": "b65d1bed-d060-4cb3-91b4-ba3cbb0b7e16-bluemix",
    "API_KEY": "vIu9HaKiRhjDxioRa24NhIKdxETRuWRJDhP8_fU9FWfc",
    "DEALERSHIP": 15
}
*/
