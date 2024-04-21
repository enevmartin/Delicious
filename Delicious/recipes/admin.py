from django.contrib import admin
from .models import Recipe
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.hashers import make_password

from ..accounts.models import Profile

User = get_user_model()

# Create users with hashed passwords
user1, created = User.objects.get_or_create(email='user1@example.com', defaults={'password': 'user1@example.comuser1@example.com'})
user2, created = User.objects.get_or_create(email='user2@example.com', defaults={'password': make_password('user2@example.comuser2@example.com')})


# Create Superusers and Staff groups
admin_group_superusers, _ = Group.objects.get_or_create(name='Superusers')
admin_group_staff, _ = Group.objects.get_or_create(name='Staff')

# Assign users to groups
admin_group_superusers.user_set.add(user1)
admin_group_staff.user_set.add(user2)

# Get permissions
add_permission = Permission.objects.get(codename='add_recipe')
change_permission = Permission.objects.get(codename='change_recipe')
delete_permission = Permission.objects.get(codename='delete_recipe')

# Assign permissions to groups
admin_group_superusers.permissions.add(add_permission, change_permission, delete_permission)
admin_group_staff.permissions.add(add_permission, change_permission)

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'creator')
    search_fields = ['title', 'creator__email']  # Update to use 'email' instead of 'username'
    list_filter = ('category',)  # Add filter by category
    ordering = ('-id',)  # Add default ordering by id
    readonly_fields = ('creator',)  # Make creator field read-only

    @staticmethod
    def creator(obj):
        return obj.creator.email
