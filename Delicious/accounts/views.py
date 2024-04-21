# accounts/views.py
from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from Delicious.accounts.forms import CustomUserCreationForm, ProfileForm
from Delicious.accounts.models import CustomUser, Profile


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


class ProfileView(DetailView):
    model = CustomUser  # or your CustomUser model
    template_name = 'accounts/my_profile.html'
    context_object_name = 'user_profile'

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return self.model.objects.get(pk=pk)


class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'accounts/edit_profile.html'
    queryset = Profile.objects.all()

    def get_success_url(self):
        return reverse_lazy('my_profile', kwargs={'pk': self.object.user.pk})


class ProfileDeleteView(DeleteView):
    model = CustomUser
    success_url = reverse_lazy('index')  # Redirect to the home page after deletion
    template_name = 'accounts/profile_confirm_delete.html'  # Create this template

    def get_object(self, queryset=None):
        return self.request.user  # Delete the logged-in user's profile

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    form_class = AuthenticationForm


def custom_logout(request):

    logout(request)

    return redirect('index')

