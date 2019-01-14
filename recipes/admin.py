from django.contrib import admin

# Register your models here.
from django.contrib import admin
from adminsortable2.admin import SortableInlineAdminMixin
from .models import Recipes, Utilities, Ingredients, Steps, IngredientsAmount, Unit, Labels, Processed
from django import forms


class StepsAdmin(SortableInlineAdminMixin, admin.StackedInline):
    model = Steps
    extra = 0

class IngredientAdmin(admin.ModelAdmin):
    search_fields = ['name']
    ordering = ['name']

class IngrAdmin(SortableInlineAdminMixin, admin.TabularInline):
    model = IngredientsAmount
    extra = 0
    autocomplete_fields = ['name']

class LabelsAdminForm(forms.ModelForm):
    model = Labels
    def clean_name(self):
        if ((' ' in self.cleaned_data["name"]) == True):
            raise forms.ValidationError(('Spaces not allowed'), code='invalid')
        else:
            return self.cleaned_data["name"]

class LabelsAdmin(admin.ModelAdmin):
    model = Labels
    form = LabelsAdminForm
    search_fields = ['name']

class UtilAdmin(admin.ModelAdmin):
    model = Utilities;
    search_fields = ['utility']




class RecipesAdmin(admin.ModelAdmin):
    autocomplete_fields = ['labels', 'utilities']
    inlines = [
        IngrAdmin,
        StepsAdmin

    ]



admin.site.register(Labels, LabelsAdmin)

admin.site.register(Recipes, RecipesAdmin)

admin.site.register(Utilities, UtilAdmin)
admin.site.register(Ingredients, IngredientAdmin)
admin.site.register(Unit)
admin.site.register(Processed)
