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
        return "Car make: " + self.car_make + "," + \
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
    car_type = models.CharField

    # Create a toString method for object string representation
    def __str__(self):
        return "Car make: " + self.car_make + ',' + \
                "Name: " + self.name + ',' + \
                "Dealer Id: " + self.dealership

# <HINT> Create a plain Python class `CarDealer` to hold dealer data
class CarDealer(models.Model):
    name = models.CharField(null=False, max_length=50)
    dealership = models.IntegerField(null=False)
    review = models.CharField(max_length=50)
    purchase = models.BooleanField()
    purchase_date = models.DateField()
    car_make = models.ForeignKey(CarMake, null=False, on_delete=models.CASCADE)
    car_model = models.ForeignKey(CarModel, null=False, on_delete=models.CASCADE)
    car_year = models.IntegerField(4)

    # Create a toString method for object string representation
    def __str__(self):
        return "name: " +  self.name + "," + \
                "dealership: " +  self.dealership + "," + \
                "review: " +  self.review + "," + \
                "purchase: " +  self.purchase + "," + \
                "purchase_date: " +  self.purchase_date + "," + \
                "car_make: " +  self.car_make + "," + \
                "car_model: " +  self.car_model + "," + \
                "car_year: " +  self.car_year

# <HINT> Create a plain Python class `DealerReview` to hold review data
class DealerReview(models.Model):
    city =  models.CharField(max_length=20)
    state =  models.CharField(max_length=20)
    st =  models.CharField(max_length=5)
    address =  models.TextField()
    zip =  models.CharField(max_length=6)
    lat =  models.FloatField()
    long =  models.FloatField()
    short_name =  models.CharField(max_length=20)
    full_name =  models.CharField(max_length=20)

    # Create a toString method for object string representation
    def __str__(self):
        return "city: " + self.city + "," + \
                "state: " + self.state + "," + \
                "st: " + self.st + "," + \
                "address: " + self.address + "," + \
                "zip: " + self.zip + "," + \
                "lat: " + self.lat + "," + \
                "long: " + self.long + "," + \
                "short_name: " + self.short_name + "," + \
                "full_name: " + self.full_name