from django.db import models

# Create your models here.
from django.db import models
import datetime
import time
import json
from PIL import Image, ImageOps
from ckeditor.fields import RichTextField

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
    description = RichTextField()
    utilities = models.ManyToManyField(Utilities, blank=True)
    labels = models.ManyToManyField(Labels)
    forPeople = models.IntegerField(default=2)
    cKal = models.IntegerField(default=0)
    timeToMake = models.IntegerField(blank=True, default=20)
    timeToMakeActive = models.IntegerField(blank=True, default=20)
    image = models.ImageField(null=True, blank=True, upload_to="recipesImages")

    def __str__(self):
        return self.title

    def save(self):
        super(Recipes, self).save()
        if(self.image):
            thumbnailSize = 900, 600
            thumbnailFile = self.image.path + ".thumbnail.jpeg"
            image = Image.open(self.image.path)
            image = ImageOps.fit(image, thumbnailSize, Image.ANTIALIAS)
            image.convert('RGB').save(thumbnailFile, 'JPEG')


class Steps(models.Model):
    stepNr = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    recipes = models.ForeignKey(Recipes, related_name='steps', on_delete=models.CASCADE)
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False)

    def __str__(self):
        return self.stepNr

    class Meta(object):
        ordering = ['my_order']

class Ingredients(models.Model):
    name = models.CharField(max_length=200)
    health = models.IntegerField(default=0, blank=True)
    separator = models.BooleanField(default=False)

    def __str__(self):
        if(self.separator):
            return self.name+" - Titel"
        else:
            return self.name


class Unit(models.Model):
    unit = models.CharField(max_length=200)

    def __str__(self):
        return self.unit


class Processed(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class IngredientsAmount(models.Model):
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False)
    name = models.ForeignKey(Ingredients, on_delete=models.CASCADE)
    recipes = models.ForeignKey(Recipes, related_name='ingredients', on_delete=models.CASCADE, blank=True)
    amount = models.FloatField(default=0, blank=True, null=True)
    unit = models.ForeignKey(Unit, on_delete=models.DO_NOTHING, blank=True, null=True)
    processed = models.ForeignKey(Processed, on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return str(self.amount)+' '+str(self.unit)+' '+str(self.name)

    class Meta(object):
        ordering = ['my_order']

