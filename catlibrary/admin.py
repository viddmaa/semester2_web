from django.contrib import admin
from .models import Breed, Tag


@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    list_display = ('name', 'average_weight', 'life_expectancy', 'created_at')
    search_fields = ('name',)

admin.site.register(Tag)