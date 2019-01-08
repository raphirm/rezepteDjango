from django.db import models

# Create your models here.
from django.db import models
import datetime
import time


class Labels(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Utilities(models.Model):
    utility = models.CharField(max_length=200)
    utilityPic = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.utility


class Recipes(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    utilities = models.ManyToManyField(Utilities, blank=True)
    labels = models.ManyToManyField(Labels)
    forPeople = models.IntegerField(default=2)
    cKal = models.IntegerField(default=0)
    timeToMake = models.IntegerField(blank=True, default=20)

    def __str__(self):
        return self.title


class Steps(models.Model):
    stepNr = models.IntegerField()
    description = models.TextField()
    recipes = models.ForeignKey(Recipes, on_delete=models.CASCADE)

    def __str__(self):
        return self.stepNr


class Ingredients(models.Model):
    name = models.CharField(max_length=200)
    health = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Unit(models.Model):
    unit = models.CharField(max_length=200)

    def __str__(self):
        return self.unit


class IngredientsAmount(models.Model):
    name = models.ForeignKey(Ingredients, on_delete=models.CASCADE)
    recipes = models.ForeignKey(Recipes, on_delete=models.CASCADE)
    amount = models.IntegerField()
    unit = models.ForeignKey(Unit, on_delete=models.DO_NOTHING)



