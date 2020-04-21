from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.


class candidat(models.Model):
    nom = models.CharField(max_length=30,blank=False)
    prenom = models.CharField(max_length=30,blank=False)
    Email = models.EmailField(max_length=200,blank=False,unique=True)
    etat = models.EmailField(default="Nouvelle")
    Date_de_naissance = models.DateField(blank=True)
    num_tel = models.CharField(max_length=8,blank=False,unique=True)
    Disponibilite = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(6)])
    status_email = models.CharField(max_length=30,blank=True)
    Nb_années_expérience = models.IntegerField(validators=[MinValueValidator(0)])
    cv = models.FileField(blank=False)
    message = models.TextField(blank=True)

