from django.db import models

class Body_info(models.Model):
    name = models.CharField(max_length=100,help_text="The name of the Player.")
    Height = models.IntegerField("enter your height")
    Weight = models.IntegerField("enter your weight")
    age = models.IntegerField("enter your age")
    calories = ''





