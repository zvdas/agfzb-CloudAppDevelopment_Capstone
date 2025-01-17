from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
import logging
import json
# from .models import related models
from .models import *
# from .restapis import related methods
from .restapis import *
# from .restapis import get_dealer_by_id_from_cf, get_dealer_reviews_from_cf, get_dealers_from_cf, post_request

# Get an instance of a logger
logger = logging.getLogger(__name__)

# Create your views here.

# Create an `about` view to render a static about page
def about(request):
    context = {}
    # if the request method is get
    if request.method == 'GET':
        return render(request, 'djangoapp/about_us.html')

# Create a `contact` view to return a static contact page
def contact(request):
    context = {}
    # if the request method is get
    if request.method == 'GET':
        return render(request, 'djangoapp/contact_us.html')

# Create a `login_request` view to handle sign in request
def login_request(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['psw']
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('djangoapp:about')
        else:
            context['message'] = "Invalid username or password."
            return render(request, 'djangoapp/user_login.html', context)
    else:
        return render(request, 'djangoapp/user_login.html', context)

# Create a `logout_request` view to handle sign out request
def logout_request(request):
    logout(request)
    # return redirect('djangoapp/')
    return render(request, 'djangoapp/user_login.html')

# Create a `registration_request` view to handle sign up request
def registration_request(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'djangoapp/user_registration.html', context)
    elif request.method == 'POST':
        # Check if user exists
        username = request.POST['username']
        password = request.POST['psw']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        user_exist = False
        try:
            User.objects.get(username=username)
            user_exist = True
        except:
            logger.debug("{} is new user".format(username))
        if not user_exist:
            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,password=password)
            login(request, user)
            return redirect("djangoapp")
        else:
            context['message'] = "User already exists."
            return render(request, 'djangoapp/user_registration.html', context)

# Update the `get_dealerships` view to render the index page with a list of dealerships
def get_dealerships(request):
    context = {}
    if request.method == "GET":
        # url = "http://localhost:3000/get_dealer"
        url = "https://us-south.functions.appdomain.cloud/api/v1/web/1605f0b5-46d6-4197-b171-3e165a3753a8/dealerships/get-dealerships.json"
        # Get dealers from the URL
        dealerships = get_dealers_from_cf(url)
        # Concat all dealer's short name
        # dealer_names = ' '.join([dealer.short_name for dealer in dealerships])
        context = {'dealership_list': [dealer for dealer in dealerships]}
        # Return a list of dealer short name
        # return HttpResponse(dealer_names)
        return render(request, 'djangoapp/index.html', context)


# Create a `get_dealer_details` view to render the reviews of a dealer
def get_dealer_details(request, dealer_id, dealer_name):
    context = {}
    if request.method == "GET":
        # url = "http://localhost:3000/get_review"
        url = "https://us-south.functions.appdomain.cloud/api/v1/web/1605f0b5-46d6-4197-b171-3e165a3753a8/dealerships/get-reviews.json"
        reviews = get_dealer_reviews_from_cf(url, dealer_id)
        # dealer_reviews = [review.review for review in reviews]
        context = {"reviews": [review for review in reviews['reviews']], "dealer_id": dealer_id, "dealer_name": dealer_name}
        # return HttpResponse(dealer_reviews)
        return render(request, 'djangoapp/dealer_details.html', context)

# Create a `add_review` view to submit a review
# def add_review(request, dealer_id):
def add_review(request, dealer_id, dealer_name):
    context = {}
    if request.method == "GET":
        # url = "http://localhost:3000/get_review_by_dealership"
        url = "https://us-south.functions.appdomain.cloud/api/v1/web/1605f0b5-46d6-4197-b171-3e165a3753a8/dealerships/get-reviews.json"
        reviews = get_dealer_reviews_from_cf(url, dealer_id)
        # print("reviews: ", reviews)
        context = {"cars": [review for review in reviews['reviews']], "dealer_id": dealer_id, "dealer_name": dealer_name, "length": reviews['length']}
        return render(request, 'djangoapp/add_review.html', context)
    if request.method == "POST":
        url = "https://us-south.functions.appdomain.cloud/api/v1/web/1605f0b5-46d6-4197-b171-3e165a3753a8/dealerships/post-review.json"
        # url = "http://localhost:3000/post_review"
        review = request.POST['content']
        print("length: ", request.POST['purchasecheck'])
        id = int(request.POST['id']) + 1
        purchase = True if request.POST['purchasecheck'] == 'on' else False
        car_model = request.POST['car'].split('-')[0]
        car_make = request.POST['car'].split('-')[1]
        car_year = request.POST['car'].split('-')[2]
        purchase_date  = request.POST['purchasedate']
        json_payload = {
            "id": id,
            "name" : dealer_name,
            "dealership": dealer_id,
            "review": review,
            "purchase": purchase,
            "purchase_date": purchase_date,
            "car_make": car_make,
            "car_model": car_model,
            "car_year": car_year
        }
        print("payload: ", json_payload)
        post_request(url, json_payload)
        return redirect("djangoapp:dealer_details", dealer_id=dealer_id, dealer_name=dealer_name)