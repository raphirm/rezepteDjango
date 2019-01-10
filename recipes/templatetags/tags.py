from django.template import Library

from rest_framework import serializers
register = Library()
from .. import serializers
import json

@register.filter
def jsona(queryset):
     json_data = serializers.RecipesSerializer(queryset, many=True).data

     return json.dumps(json_data)
