# accounts/views.py
from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from Delicious.accounts.forms import CustomUserCreationForm


class SignUpView(CreateView):
    template_name = 'accounts/signup.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, form.instance)
        # user = form.save()
        return result

    # def form_valid(self, form):
    #     form.save()
    #     return super().form_valid(form)


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/my_profile.html'


class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    form_class = AuthenticationForm


def custom_logout(request):

    logout(request)

    return redirect('index')
