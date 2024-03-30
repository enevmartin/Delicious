from django.contrib import admin
from .models import CustomUser,Profile


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_active', 'is_staff')
    search_fields = ['email']


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'date_of_birth', 'profile_picture')
    search_fields = ['user__email']

    def profile_picture_preview(self, obj):
        return obj.profile_picture if obj.profile_picture else ''

    profile_picture_preview.short_description = 'Profile Picture'
