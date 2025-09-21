from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token  # <-- Import this

urlpatterns = [
    path('admin/', admin.site.urls),

    # Your API app routes
    path('', include(router.urls)),

    # ✅ Token authentication endpoint
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
