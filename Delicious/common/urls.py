from django.urls import path


from .views import ContactView, SubscribeNewsletterView, CommentListView, AllRecipeListView

#
urlpatterns = [
    # path('about/', AboutView.as_view(), name='about'),
    # path('blog/', BlogPostView.as_view(), name='blog-post'),
    path('contact/', ContactView.as_view(), name='contact'),
    # path('elements/', ElementsView.as_view(), name='elements'),  # Rename to 'elements'
    # path('recipe-post/', RecipePostView.as_view(), name='recipe-post'),
    path('comments/',CommentListView.as_view(), name='show_comments'),
    path('subscribe-newsletter/', SubscribeNewsletterView.as_view(), name='subscribe_newsletter'),
    path('all-recipes/', AllRecipeListView.as_view(), name='all_recipes'),
]
