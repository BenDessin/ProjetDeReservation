from django.db import models
from django.contrib.auth import get_user_model
from profil.models import ProfilUser

User = get_user_model()

# Create your models here.

#nouveau
class Price(models.Model):
    prix = models.CharField(max_length=255, verbose_name="prix")
    def __str__(self):
        return self.prix

class Dimension(models.Model):
    taille = models.CharField(max_length=255, verbose_name="format")
    def __str__(self):
        return self.taille
    
class Cathegorie(models.Model):
    cathegorie = models.CharField(max_length=255, verbose_name="cathegorie")
    def __str__(self):
        return self.cathegorie
#endnouveau

class Cadre(models.Model):
    titre = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to="post/%y")
    description = models.CharField(max_length=255, blank=True, null=True)#modifier
    format = models.ForeignKey(Dimension, on_delete=models.SET_NULL, null=True)#modifier
    prix = models.ForeignKey(Price, on_delete=models.SET_NULL, null=True)#modifier
    cathegorie = models.ForeignKey(Cathegorie, on_delete=models.SET_NULL, null=True)#modifier

class Reservation(models.Model):
    nom = models.CharField(max_length=255)
    numero = models.CharField(max_length=255,null=False)
    residence = models.CharField(max_length=255,null=False)
    image = models.ImageField(upload_to="reservation/%y")
    format = models.ForeignKey(Dimension, on_delete=models.SET_NULL, null=True)
    event = models.CharField(max_length=255)
    date = models.DateField(auto_now=True)
    date_remise = models.DateField(blank=True)
    auth = models.ForeignKey(ProfilUser, on_delete=models.CASCADE, null=True)
    cathegorie = models.ForeignKey(Cathegorie, on_delete=models.SET_NULL, null=True)#modifier
    
    class Meta:
        ordering = ['-date']
        verbose_name = "Reservation"
    
    def __str__(self):
        return self.nom