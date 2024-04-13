# recipes/views.py
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Recipe


class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipes/recipe_list.html'
    context_object_name = 'recipes'


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipes/recipe_detail.html'
    context_object_name = 'recipe'


class RecipeCreateView(CreateView):
    model = Recipe
    template_name = 'recipes/recipe_form.html'
    fields = ['title', 'ingredients', 'instructions']
    success_url = '/recipes/'  # Redirect to recipe list after successful creation


class RecipeUpdateView(UpdateView):
    model = Recipe
    template_name = 'recipes/recipe_form.html'
    fields = ['title', 'ingredients', 'instructions']
    success_url = '/recipes/'  # Redirect to recipe list after successful update


class RecipeDeleteView(DeleteView):
    model = Recipe
    template_name = 'recipes/recipe_confirm_delete.html'
    success_url = '/recipes/'  # Redirect to recipe list after successful deletion
