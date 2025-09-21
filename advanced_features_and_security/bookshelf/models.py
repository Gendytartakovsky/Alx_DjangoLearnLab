from django.db import models
from django.conf import settings  # Use this for referencing CustomUser

# ------------------------------
# Book Model
# ------------------------------
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100, blank=True, null=True)
    borrowed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # <- points to CustomUser
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    borrowed_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    returned_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title
