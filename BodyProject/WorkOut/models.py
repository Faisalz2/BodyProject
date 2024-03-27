from django.db import models

class Body_info(models.Model):
    name = models.CharField(max_length=100,help_text="The name of the Player.")
    Height = models.IntegerField("enter your height")
    Weight = models.IntegerField("enter your weight")
    age = models.IntegerField("enter your age")

    def calculate_calories(self):
        
        bmr = 10 * self.Weight + 6.25 * self.Height - 5 * self.age + 5
        calories = bmr * 1.2  
        return calories

    def __str__(self):
        return self.name




