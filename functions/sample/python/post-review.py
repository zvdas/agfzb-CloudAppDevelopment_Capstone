# from cloudant import Cloudant
from cloudant.client import Cloudant

def main(dict):
    client = Cloudant.iam(account_name=dict['ACCOUNT_NAME'], api_key=dict['API_KEY'], connect=True)
    # Create document content data
    data = {
        # "id": 1, # Setting _id is optional
        "name": "John Doe",
        "dealership": 15,
        "review": "Total grid-enabled service-desk",
        "purchase": true,
        "purchase_date": "07/11/2020",
        "car_make": "Audi",
        "car_model": "A6",
        "car_year": 2010
        }

    # Create a document using the Database API
    my_document = client['reviews'].create_document(data)

    # Check that the document exists in the database
    if my_document.exists():
        return {"review": my_document}