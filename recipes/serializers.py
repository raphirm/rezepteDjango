from django.template import Library

from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
register = Library()
from . import models
import json


class UtilitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Utilities
        depth = 1
        fields = (
            'utility', 'utilityPic'
        )


class LabelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Labels
        depth = 1
        fields = (
            'name',
        )


class RecipesSerializer(serializers.ModelSerializer):
  #  utilities = UtilitiesSerializer(many=True)
   # labels = LabelsSerializer(many=True)
    class Meta:
        model = models.Recipes
        depth = 3
        fields = (
            'id',
            'title',
            'description',
            'utilities',
            'labels',
            'forPeople',
            'cKal',
            'timeToMake',
            'timeToMakeActive',
            'image',
            'ingredients',
            'steps',
        )


