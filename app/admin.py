from django.contrib import admin
from .models import Recipe

# Register your models here.
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['id','Title','Category','author','created_at','updated_at','image']