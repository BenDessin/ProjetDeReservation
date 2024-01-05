from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from profil.models import ProfilUser

User = get_user_model()

# Create your models here.
dimension = (
    ("format A4(20cm X 30cm)","format A4(20cm X 30cm)"),
    ("format A3(30cm X 40cm)","format A3(30cm X 40cm)"),
    ("format A2(40cm X 60cm)","format A2(40cm X 60cm)"),
    ("format A1(60cm X 100cm)","format A1(60cm X 100cm)"),
)

class Cadre(models.Model):
    titre = models.CharField(max_length=255)
    image = models.ImageField(upload_to="post/%y")
    description = models.CharField(max_length=255)
    format = models.CharField(max_length=255, choices=dimension)

class Reservation(models.Model):
    nom = models.CharField(max_length=255)
    numero = models.CharField(max_length=255,null=False)
    residence = models.CharField(max_length=255,null=False)
    image = models.ImageField(upload_to="reservation/%y")
    format = models.CharField(max_length=255, choices=dimension)
    event = models.CharField(max_length=255)
    date = models.DateField(auto_now=True)
    date_remise = models.DateField(blank=True)
    auth = models.ForeignKey(ProfilUser, on_delete=models.CASCADE, null=True)
    
    class Meta:
        ordering = ['-date']
        verbose_name = "Reservation"
    
    def __str__(self):
        return self.nom
        
    