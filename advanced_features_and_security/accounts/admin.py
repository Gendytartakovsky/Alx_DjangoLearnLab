from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# ------------------------------
# Custom UserAdmin
# ------------------------------
class CustomUserAdmin(UserAdmin):
    """
    Define admin model for CustomUser.
    Adds 'date_of_birth' and 'profile_photo' to list, add, and edit views.
    """

    # Columns to display in the user list in admin
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'date_of_birth')

    # Fields to display when editing a user
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )

    # Fields to display when creating a new user
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )

# ------------------------------
# Register CustomUser with the custom admin
# ------------------------------
admin.site.register(CustomUser, CustomUserAdmin)
