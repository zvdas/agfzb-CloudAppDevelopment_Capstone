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