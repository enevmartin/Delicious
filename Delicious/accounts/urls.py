# accounts/urls.py
from django.urls import path

from Delicious.accounts.views import SignUpView, custom_logout, ProfileView, CustomLoginView, ProfileUpdateView, \
    ProfileDeleteView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', custom_logout, name='logout'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='my_profile'),
    path('profile/<int:pk>/edit/', ProfileUpdateView.as_view(), name='edit_profile'),
    path('profile/<int:pk>/delete/', ProfileDeleteView.as_view(), name='delete_profile'),
    # Add other account-related URLs here as needed
]
