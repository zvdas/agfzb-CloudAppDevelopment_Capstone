#
#
# main() will be run when you invoke this action
#
# @param Cloud Functions actions accept a single parameter, which must be a JSON object.
#
# @return The output of this action, which must be a JSON object.
#
#
# from cloudant import Cloudant
from cloudant.client import Cloudant

def main(dict):
    client = Cloudant.iam(account_name=dict['ACCOUNT_NAME'], api_key=dict['API_KEY'], connect=True)
    
    selector = {'dealership': {'$eq': dict['DEALERSHIP']}}
    return client['reviews'].get_query_result(selector)


{
    "ACCOUNT_NAME": "b65d1bed-d060-4cb3-91b4-ba3cbb0b7e16-bluemix",
    "API_KEY": "vIu9HaKiRhjDxioRa24NhIKdxETRuWRJDhP8_fU9FWfc",
    "DEALERSHIP": 15
}