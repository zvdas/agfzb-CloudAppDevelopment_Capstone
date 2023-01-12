from .models import CarMake

def write_car_makes():
    # create a car make
    car_make_first = CarMake(car_make='Audi', car_description='A6')
    car_make_first.save()
    
    car_make_second = CarMake(car_make='BMW', car_description='X3')
    car_make_second.save()
    
    car_make_third = CarMake(car_make='Lexus', car_description='CX')
    car_make_third.save()


    print("Car objects all saved... ")
