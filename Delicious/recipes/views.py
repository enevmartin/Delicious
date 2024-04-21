# recipes/views.py
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from .forms import RecipeForm
from .models import Recipe
from ..accounts.models import Profile


class AllRecipeListView(ListView):
    model = Recipe
    template_name = 'recipes/all_recipe_list.html'
    context_object_name = 'recipes'


class MyRecipeListView(ListView):
    model = Recipe
    template_name = 'recipes/my_recipe_list.html'
    context_object_name = 'recipes'

    def get_queryset(self):
        queryset = super().get_queryset()
        # Filter the queryset to only include recipes authored by the current user
        profile = self.request.user.profile
        queryset = queryset.filter(creator=profile)
        return queryset


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipes/recipe_detail.html'
    context_object_name = 'recipe'





class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        user = self.request.user
        profile = Profile.objects.get(user=user)  # Retrieve the associated profile
        form.instance.creator = profile  # Assign the profile to the creator field
        return super().form_valid(form)


class RecipeUpdateView(UpdateView):
    model = Recipe
    template_name = 'recipes/edit_recipe.html'
    form_class = RecipeForm

    def get_success_url(self):
        return reverse_lazy('recipe_detail', kwargs={'pk': self.object.pk})


class RecipeDeleteView(DeleteView):
    model = Recipe
    template_name = 'recipes/recipe_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('my_recipes', kwargs={'pk': self.object.pk})


def search_recipes(request):
    query = request.GET.get('search')
    user_profile = request.user.profile
    context = request.GET.get('context')  # Added to determine the search context

    if context == 'all':
        # Search in all recipes
        if query:
            recipes = Recipe.objects.filter(title__icontains=query)
        else:
            recipes = Recipe.objects.all()
        template = 'recipes/all_recipe_list.html'
    else:
        # Search in user's recipes
        if query:
            recipes = Recipe.objects.filter(title__icontains=query, creator=user_profile)
        else:
            recipes = Recipe.objects.filter(creator=user_profile)
        template = 'recipes/my_recipe_list.html'

    return render(request, template, {'recipes': recipes})





class RecipeCountView(TemplateView):
    template_name = 'recipes/all_recipe_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get all unique category choices
        categories = dict(Recipe.CATEGORY_CHOICES)

        # Create a dictionary to store category counts
        counts_dict = {}

        # Count recipes for each category
        for category, _ in Recipe.CATEGORY_CHOICES:
            count = Recipe.objects.filter(category=category).count()
            counts_dict[categories[category]] = count

        # Add counts dictionary to context
        context['counts_dict'] = counts_dict
        return context

