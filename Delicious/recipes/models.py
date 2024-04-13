# recipes/models.py
from django.db import models

from Delicious.accounts.models import Profile


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    ingredients = models.TextField()
    instructions = models.TextField()
    creator = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
