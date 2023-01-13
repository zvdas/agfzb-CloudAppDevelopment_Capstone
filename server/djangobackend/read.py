# Django specific settings
import inspect
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangobackend.settings")
from django.db import connection

# Ensure settings are read
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from djangoapp.models import *
from datetime import date

# Find all car makes
car_makes = CarMake.objects.all()
print(car_makes)

car_models = CarModel.objects.all()
print(car_models)

car_dealers = CarDealer.objects.all()
print(car_dealers)

dealer_reviews = DealerReview.objects.all()
print(dealer_reviews)