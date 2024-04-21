from django.urls import path

from . import views
from .views import (
    AllRecipeListView,
    MyRecipeListView,
    RecipeDetailView,
    RecipeCreateView,
    RecipeUpdateView,
    RecipeDeleteView,
    RecipeCountView,
)

urlpatterns = [
    path('all-recipes/', AllRecipeListView.as_view(), name='all_recipes'),
    path('my-recipes/<int:pk>/', MyRecipeListView.as_view(), name='my_recipes'),  # Include the pk parameter
    path('<int:pk>/', RecipeDetailView.as_view(), name='recipe_detail'),
    path('create/', RecipeCreateView.as_view(), name='recipe_create'),
    path('<int:pk>/update/', RecipeUpdateView.as_view(), name='recipe_update'),
    path('<int:pk>/delete/', RecipeDeleteView.as_view(), name='recipe_delete'),
    path('search/', views.search_recipes, name='search_recipes'),
    # path('search/', views.search_all_recipes, name='search_all_recipes'),

    path('recipe-counts/', RecipeCountView.as_view(), name='recipe_counts'),
]
