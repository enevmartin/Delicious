from django.contrib import admin
from .models import Recipe


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'creator')
    search_fields = ['title', 'creator__username']

    @staticmethod
    def creator(obj):
        return obj.creator.username
