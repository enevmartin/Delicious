from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import FormView

from .forms import CommentForm
from .models import Comment, NewsletterSubscriber
from ..recipes.models import Recipe


def custom_404_view(request):
    return render(request, '404.html', status=404)


def custom_500_view(request):
    return render(request, '500.html', status=500)


class AllRecipeListView(ListView):
    model = Recipe
    template_name = 'common/index.html'
    context_object_name = 'recipes'


class ContactView(FormView):
    template_name = 'recipes/all_recipe_list.html'
    form_class = CommentForm
    success_url = reverse_lazy('all_recipes')  # Adjust the URL name as per your project's URL configuration

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class IndexView(TemplateView):
    template_name = 'common/index.html'  # Template for the home page


# views.py


class CommentListView(ListView):
    model = Comment
    template_name = 'recipes/all_recipe_list.html'
    context_object_name = 'comment_list'  # Set the context name to 'comment_list'

    def get_queryset(self):
        queryset = super().get_queryset()  # Get the base queryset
        # You can add any additional filtering or ordering here if needed
        return queryset


class SubscribeNewsletterView(View):
    @staticmethod
    def post(request):
        email = request.POST.get('email')
        if email:
            # Try to get the subscriber object or create it if it doesn't exist
            _, created = NewsletterSubscriber.objects.get_or_create(email=email)
            if created:
                pass
        return redirect('index')
