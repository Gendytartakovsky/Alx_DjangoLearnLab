from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

# ------------------------------
# Custom User Manager
# ------------------------------
class CustomUserManager(BaseUserManager):
    """Manager for CustomUser to handle user creation"""

    def create_user(self, username, email, password=None, date_of_birth=None, **extra_fields):
        """
        Create and save a regular user with username, email, password, and optional date_of_birth.
        """
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)
        user = self.model(
            username=username,
            email=email,
            date_of_birth=date_of_birth,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, date_of_birth=None, **extra_fields):
        """
        Create and save a superuser with all necessary permissions.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True")

        return self.create_user(username, email, password, date_of_birth=date_of_birth, **extra_fields)


# ------------------------------
# Custom User Model
# ------------------------------
class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    # Link the custom manager
    objects = CustomUserManager()

    def __str__(self):
        return self.username

