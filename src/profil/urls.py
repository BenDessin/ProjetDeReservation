from django.urls import path, include
from .views import signup

app_name = "profil"

urlpatterns = [
    path("Enregistrer/", signup, name="creer_profil"),
    path('compte/', include('django.contrib.auth.urls')),
]