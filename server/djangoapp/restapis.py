import requests
import json
# import related models here
from .models import *
from requests.auth import HTTPBasicAuth
# for sentiments (NLU)
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions

# Create a `get_request` to make HTTP GET requests
# e.g., response = requests.get(url, params=params, headers={'Content-Type': 'application/json'}, auth=HTTPBasicAuth('apikey', api_key))
def get_request(url, **kwargs):
    print("GET from {}, {} ".format(url, kwargs))
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(url, headers={'Content-Type': 'application/json'}, params=kwargs)
    except:
        # If any error occurs
        print("Network exception occurred")
    status_code = response.status_code
    print("With status {} ".format(status_code))
    json_data = json.loads(response.text)
    return json_data

# Create a `post_request` to make HTTP POST requests
# e.g., response = requests.post(url, params=kwargs, json=payload)
def post_request(url, payload):
    print(payload)
    print("Post to {} ".format(url))
    try:
        # Call post method of requests library with URL and parameters
        # requests.post(url, headers={'Content-Type': 'application/json'}, json=payload, auth="QECPIMEVRl6PYqapP84trF4bOtHc1aKx4DEAH6wJHgxR")
        requests.post(url, json=payload)
    except:
        # If any error occurs
        print("Network exception occurred")
    # status_code = response.status_code
    # print("With status {} ".format(status_code))
    # print("With status {} ".format(response))
    # json_data = json.loads(response.text)
    # return json_data
    # return response

# Create a get_dealers_from_cf method to get dealers from a cloud function
# def get_dealers_from_cf(url, **kwargs):
# - Call get_request() with specified arguments
# - Parse JSON results into a CarDealer object list
def get_dealers_from_cf(url):
    results = []
    # Call get_request with a URL parameter
    json_result = get_request(url)
    if json_result:
        # Get the row list in JSON as dealers
        dealers = json_result["result"]
        # dealers = json_result["result"]["rows"]
        # For each dealer object
        for dealer in dealers:
            # Get its content in `doc` object
            dealer_doc = dealer["doc"]
            # Create a CarDealer object with values in `doc` object
            dealer_obj = CarDealer(address=dealer_doc["address"], city=dealer_doc["city"], full_name=dealer_doc["full_name"],
                                   id=dealer_doc["id"], lat=dealer_doc["lat"], long=dealer_doc["long"],
                                   short_name=dealer_doc["short_name"], state=dealer_doc["state"], 
                                   st=dealer_doc["st"], zip=dealer_doc["zip"])
            results.append(dealer_obj)
    return results

# Create a get_dealer_reviews_from_cf method to get reviews by dealer id from a cloud function
# def get_dealer_by_id_from_cf(url, dealerId):
# - Call get_request() with specified arguments
# - Parse JSON results into a DealerView object list
def get_dealer_reviews_from_cf(url, dealerId):
    # get reviews by dealer id
    json_result = [x['doc'] for x in get_request(url)['rows'] if x['doc']['dealership']==dealerId]
    # print("json result: ", json_result)
    # print("length: ", get_request(url)["total_rows"])
    review_object = {"reviews": [
        DealerReview(
            id=x['id'], car_make=x['car_make'], car_model=x['car_model'], 
            car_year=x['car_year'], dealership=x['dealership'], name=x['name'], 
            purchase=x['purchase'], purchase_date=x['purchase_date'], review=x['review'],
            sentiment=analyze_review_sentiments(x['review'])
        ) for x in json_result if json_result
    ], "length": get_request(url)["total_rows"]}
    # dealer_reviews = [x['review'] for x in json_result]
    # review_object.sentiment = analyze_review_sentiments(dealer_reviews)
    return review_object

# Create an `analyze_review_sentiments` method to call Watson NLU and analyze text
# def analyze_review_sentiments(text):
# - Call get_request() with specified arguments
# - Get the returned sentiment label such as Positive or Negative
def analyze_review_sentiments(dealer_review):
    api_key = "ABOF830O7Z12X_N5C6YMtfkCLhzDfglSryt5xMWFgN3s"
    url = "https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/instances/8e239f8f-8732-4438-a5b6-beea2f0f9e0b"
    authenticator = IAMAuthenticator(api_key)
    natural_language_understanding = NaturalLanguageUnderstandingV1(
        version='2022-04-07',
        authenticator=authenticator
    )
    natural_language_understanding.set_service_url(url)
    response = natural_language_understanding.analyze(
        text = dealer_review,
        features = Features(entities=EntitiesOptions(emotion=False, sentiment=True, limit=3),
        keywords=KeywordsOptions(emotion=False, sentiment=True, limit=3))
    ).get_result()
    # sentiment =  'positive' if response["keywords"][0]['relevance'] > 0.5 else 'negative' if response["keywords"][0]['relevance'] < 0.5 else 'neutral'
    sentiment =  response["keywords"][0]['relevance']
    # print("sentiment: ", sentiment)
    return sentiment
