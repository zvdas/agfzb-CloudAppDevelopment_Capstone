# python 3.9
from ibmcloudant.cloudant_v1 import CloudantV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

def main(dict):
    authenticator = IAMAuthenticator(dict['API_KEY'])
    service = CloudantV1(authenticator=authenticator)
    service.set_service_url(dict['COUCH_URL'])
    products_doc = Document(
        name = dict['name'],
        dealership = dict['dealership'],
        review = dict['review'],
        purchase = dict['purchase'],
        purchase_date = dict['purchase_date'],
        car_make = dict['car_make'],
        car_model  = dict['car_model'],
        car_year = dict['car_year']
    )

    response = service.post_document(db='reviews', document=reviews_doc).get_result()
    return response


# python 3.7
# from cloudant import Cloudant
from cloudant.client import Cloudant

def main(dict):
    client = Cloudant.iam(account_name=dict['ACCOUNT_NAME'], api_key=dict['API_KEY'], connect=True)
    # Create document content data
    data = {
        # "id": 1, # Setting _id is optional
        "name": dict['name'],
        "dealership": dict['dealership'],
        "review": dict['review'],
        "purchase": dict['purchase'],
        "purchase_date": dict['purchase_date'],
        "car_make": dict['car_make'],
        "car_model": dict['car_model'],
        "car_year": dict['car_year']
        }

    # Create a document using the Database API
    my_document = client['reviews'].create_document(data)

    # Check that the document exists in the database
    if my_document.exists():
        return {"review": my_document}


{
    "ACCOUNT_NAME": "b65d1bed-d060-4cb3-91b4-ba3cbb0b7e16-bluemix",
    "API_KEY": "vIu9HaKiRhjDxioRa24NhIKdxETRuWRJDhP8_fU9FWfc",
    "name": "John Doe",
    "dealership": 15,
    "review": "Total grid-enabled service-desk",
    "purchase": true,
    "purchase_date": "07/11/2020",
    "car_make": "Audi",
    "car_model": "A6",
    "car_year": 2010
}
