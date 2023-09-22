from django.db import models
from django_mysql.models import ListCharField

# Create your models here.

class Ecole(models.Model):
    nom = models.CharField(max_length=255)
    email = models.EmailField()
    description = models.TextField()
    note = models.FloatField()
    contact = models.CharField(max_length=16)
    image = models.ImageField(upload_to="ecoles", height_field=None, width_field=None, max_length=100,)


class Domaine(models.Model):
    nom = models.CharField(max_length=255)
    matieres_principales = ListCharField(
        base_field=models.CharField(max_length=32),
        size=4,
        max_length=(4*33)
        
    )
    image = models.ImageField(upload_to="domaines", height_field=None, width_field=None, max_length=100,)


class Enseigne(models.Model):
    domaine = models.ForeignKey(Domaine, on_delete=models.CASCADE)
    ecole = models.ForeignKey(Ecole, on_delete=models.CASCADE)
    duration = models.IntegerField()
    prix = models.IntegerField()

class Metier (models.Model):
    name = models.CharField(max_length=255)
    salaire = models.IntegerField()
    description = models.TextField()
    qualite = ListCharField(
        base_field=models.CharField(max_length=32),
        size=4,
        max_length=(4*33)
    )
    image = models.ImageField(upload_to="metiers", height_field=None, width_field=None, max_length=100,)

class Reponse (models.Model):
    reponse = models.CharField(max_length=255)
    
class Question (models.Model):
    question = models.TextField()
    
