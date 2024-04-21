from django.db import models
from Delicious.accounts.models import Profile


class Recipe(models.Model):
    CATEGORY_CHOICES = [
        ('BBQ', 'BBQ'),
        ('Breakfast', 'Breakfast'),
        ('Lunch', 'Lunch'),
        ('Dinner', 'Dinner'),
        ('Appetizers', 'Appetizers'),
    ]

    title = models.CharField(max_length=100)
    ingredients = models.TextField()
    instructions = models.TextField()
    creator = models.ForeignKey(Profile, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='recipe_pictures', null=True, blank=True)
    preparation_time = models.CharField(max_length=50, null=True, blank=True)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default=' ')

    def __str__(self):
        return self.title


