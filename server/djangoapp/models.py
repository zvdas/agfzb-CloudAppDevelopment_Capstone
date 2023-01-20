from django.db import models
from django.utils.timezone import now

# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
class CarMake(models.Model):
    car_make = models.CharField(null=False, max_length=50)
    car_description = models.CharField(max_length=500)

    # Create a toString method for object string representation
    def __str__(self):
        return \
            "Car make: " + self.car_make + "," + \
            "Car description: " + self.car_description



# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, null=True, on_delete=models.CASCADE)
    name = models.CharField(null=False, max_length=50)
    dealership = models.IntegerField(null=False)
    SEDAN = 'Sedan'
    HATCHBACK = 'Hatchback'
    SUV = 'SUV'
    WAGON = 'Wagon'
    JEEP = 'Jeep'
    MUV = 'MUV'
    TYPE_CHOICES = [
        (SEDAN, 'Sedan'),
        (HATCHBACK, 'Hatchback'),
        (SUV, 'SUV'),
        (WAGON, 'Wagon'),
        (JEEP, 'Jeep'),
        (MUV, 'MUV')
    ]
    car_type = models.CharField(null=False, max_length=20, choices=TYPE_CHOICES, default=SEDAN)
    year = models.DateField(null=True)

    # Create a toString method for object string representation
    def __str__(self):
        return \
            "Car make: " + str(self.car_make) + ',' + \
            "Name: " + self.name + ',' + \
            "Dealer Id: " + str(self.dealership) + ',' + \
            "Car Type" + self.car_type + ',' + \
            "Year" + str(self.year)

# <HINT> Create a plain Python class `CarDealer` to hold dealer data
class CarDealer:

    def __init__(self, address, city, full_name, id, lat, long, short_name, state, st, zip):
        # Dealer address
        self.address = address
        # Dealer city
        self.city = city
        # Dealer Full Name
        self.full_name = full_name
        # Dealer id
        self.id = id
        # Location lat
        self.lat = lat
        # Location long
        self.long = long
        # Dealer short name
        self.short_name = short_name
        # Dealer state
        self.state = state
        # Dealer state (short)
        self.st = st
        # Dealer zip
        self.zip = zip

    def __str__(self):
        return "Dealer name: " + self.full_name

# <HINT> Create a plain Python class `DealerReview` to hold review data
class DealerReview:

    def __init__(self, id, dealership, name, purchase, review, purchase_date, car_make, car_model, car_year, sentiment):
        # Review id
        self.id = id
        # Dealership id
        self.dealership = dealership
        # Reviewer name
        self.name = name
        # Dealer purchase
        self.purchase = purchase
        # Dealer review
        self.review = review
        # Dealer purchase date
        self.purchase_date =  purchase_date
        # Dealer car make
        self.car_make = car_make
        # Dealer car model
        self.car_model = car_model
        # Dealer car year
        self.car_year = car_year
        # Review sentiment
        self.sentiment = sentiment
    
    def __str__(self):
        return "Dealer review: " + self.review
