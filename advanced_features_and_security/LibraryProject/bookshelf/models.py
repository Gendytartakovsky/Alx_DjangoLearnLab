from django.db import models
from django.conf import settings  # Use this to reference CustomUser

# ------------------------------
# Library Model
# ------------------------------
class Library(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200, blank=True, null=True)
    manager = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # <- points to CustomUser
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
