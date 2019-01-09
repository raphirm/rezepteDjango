from django.contrib import admin

# Register your models here.
from django.contrib import admin
from adminsortable2.admin import SortableInlineAdminMixin
from .models import Recipes, Utilities, Ingredients, Steps, IngredientsAmount, Unit, Labels, Processed

class StepsAdmin(SortableInlineAdminMixin, admin.StackedInline):
    model = Steps
    extra = 0


class IngrAdmin(SortableInlineAdminMixin, admin.TabularInline):
    model = IngredientsAmount
    extra = 0

class RecipesAdmin(admin.ModelAdmin):
    inlines = [
        IngrAdmin,
        StepsAdmin

    ]


admin.site.register(Recipes, RecipesAdmin)

admin.site.register(Utilities)
admin.site.register(Ingredients)
admin.site.register(Unit)
admin.site.register(Labels)
admin.site.register(Processed)
