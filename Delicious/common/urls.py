from django.urls import path
from .views import AboutView, BlogPostView, ContactView, ElementsView, RecipePostView

urlpatterns = [
    path('about/', AboutView.as_view(), name='about'),
    path('blog/', BlogPostView.as_view(), name='blog-post'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('elements/', ElementsView.as_view(), name='elements'),  # Rename to 'elements'
    path('recipe-post/', RecipePostView.as_view(), name='recipe-post'),
]
