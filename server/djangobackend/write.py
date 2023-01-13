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

def write_car_makes():
    car_make_1 = CarMake(car_make='Audi', car_description='A6')
    car_make_1.save()

    car_make_2 = CarMake(car_make='BMW', car_description='X3')
    car_make_2.save()

    car_make_3 = CarMake(car_make='Lexus', car_description='CX')
    car_make_3.save()

    print("Car Makes Objects all saved")

def write_car_models():
    car_model_1 = CarModel(name='Quattro',dealership='16',car_type='sedan')
    car_model_1.save()
    
    car_model_2 = CarModel(name='GT',dealership='09',car_type='hatchback')
    car_model_2.save()
    
    car_model_3 = CarModel(name='LXS',dealership='14',car_type='suv')
    car_model_3.save()

    print("Car Models Objects all saved")

def write_car_dealers():
    car_dealer_1 = CarDealer(name='Buggatia Motor Works',dealership=2,review='Smooth car',purchase=True,purchase_date='2023-01-11',car_year=2000)
    car_dealer_1.save()
    
    car_dealer_2 = CarDealer(name='Mercedes Kravitz',dealership=16,review='Low mileage',purchase=False,purchase_date='2021-01-12',car_year=2012)
    car_dealer_2.save()
    
    car_dealer_3 = CarDealer(name='Zivotz Kove',dealership=12,review='Model discontinued',purchase=True,purchase_date='2020-11-10',car_year=2011)
    car_dealer_3.save()

    print("Car Dealer Objects all saved")

def write_dealer_reviews():
    dealer_review_1 = DealerReview(city='c1',state='s1',st='st1',address='add1',zip='zip1',lat=11.11,long=22.22,short_name='short1',full_name='full1')
    dealer_review_1.save()
    
    dealer_review_2 = DealerReview(city='c2',state='s2',st='st2',address='add2',zip='zip2',lat=22.11,long=33.22,short_name='short2',full_name='full2')
    dealer_review_2.save()
    
    dealer_review_3 = DealerReview(city='c2',state='s3',st='st3',address='add3',zip='zip3',lat=13.11,long=44.22,short_name='short3',full_name='full3')
    dealer_review_3.save()
    
    print("Dealer Review Objects all saved")

def clean_data():
    # Delete all data to start fresh
    CarMake.objects.all().delete() 
    CarModel.objects.all().delete() 
    CarDealer.objects.all().delete() 
    DealerReview.objects.all().delete() 

# clean any existing data first
clean_data()
write_car_makes()
write_car_models()
write_car_dealers()
write_dealer_reviews()