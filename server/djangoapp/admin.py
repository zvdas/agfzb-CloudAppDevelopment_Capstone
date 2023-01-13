from django.contrib import admin
# from .models import related models
from .models import CarMake
# , CarModel

# Register your models here.

# CarModelInline class
# class CarModelInline(admin.StackedInline):
    # model = CarMake
    # extra = 5

# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    fields = ['car_make','car_description']
    # inlines = [CarModelInline]

# CarModelAdmin class
# class CarModelAdmin(admin.ModelAdmin):
#     fields = ['car_make','name','dealership','car_type','year']

# Register models here
admin.site.register(CarMake, CarMakeAdmin)
# admin.site.register(CarModel, CarModelAdmin)