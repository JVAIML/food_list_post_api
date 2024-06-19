from django.db import models

# Create your models here.

class foodlistpost(models.Model):
    recipe_name = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=1000)
    ingredients = models.CharField(max_length=1000)
    food_type_values = {"veg":"veg", "non-veg":"non-veg"}
    category = models.CharField(max_length=7, choices=food_type_values, default="veg")
    method = models.CharField(max_length=1000)


    