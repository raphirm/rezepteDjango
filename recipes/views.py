from django.shortcuts import render
import json
# Create your views here.
from django.http import HttpResponse
from .models import Recipes, Utilities, Ingredients, Steps, IngredientsAmount, Unit, Labels, Processed
from django.template import loader
from django.http import Http404
from .serializers import RecipesSerializer


def index(request):
    recipes = Recipes.objects.all().prefetch_related()
    recipesComplete = Recipes.objects.all().prefetch_related('utilities').prefetch_related('labels').prefetch_related()

    context = {
        'recipes': recipes,
    }
    return render(request, 'recipes/index.html', context)

def detail(request, recipes_id):
    try:
        recipes = RecipesSerializer(Recipes.objects.get(pk=recipes_id)).data

    except Recipes.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'recipes/detail.html', {'recipes': recipes})