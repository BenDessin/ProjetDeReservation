from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.

class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('entrez un email')
        user = self.model(email = self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self, email, password=None):
        user = self.create_user(email=email, password=password)
        user.is_admin = True
        user.is_staff = True
        user.save()
        return user
        
        

class ProfilUser(AbstractBaseUser):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    telephone = models.CharField(max_length=15)
    email = models.EmailField(max_length=255, unique=True, blank=False)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    
    USERNAME_FIELD = "email"
    objects = MyUserManager()
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self,app_label):
        return True
    
