from django.db import models
from django_mysql.models import ListCharField

# Create your models here.


class Domaine(models.Model):
    name = models.CharField(max_length=255)
    matieres_principales = ListCharField(
        base_field=models.CharField(max_length=32),
        size=4,
        max_length=(4*33)

    )
    img = models.URLField(max_length=100000,)
    
    def __str__(self) -> str:
        return self.name
    fee = models.IntegerField()
    year = models.IntegerField()


class Ecole(models.Model):
    name = models.CharField(max_length=255)
    link = models.URLField()
    desc = models.TextField()
    rating = models.FloatField()
    contact = models.CharField(max_length=16)
    img = models.URLField()
    fee = models.IntegerField()
    domaine = models.ManyToManyField(Domaine,null=True)
    def __str__(self) -> str:
        return self.name



# class Enseigne(models.Model):
#     name = models.ForeignKey(Domaine, on_delete=models.CASCADE)
#     ecole = models.ForeignKey(Ecole, on_delete=models.CASCADE)
#     year = models.IntegerField()
#     fee = models.IntegerField()


class Metier (models.Model):
    name = models.CharField(max_length=255)
    salaire = models.IntegerField()
    description = models.TextField()
    qualite = ListCharField(
        base_field=models.CharField(max_length=32),
        size=4,
        max_length=(4*33)
    )
    img = models.URLField(max_length=10000,)
    domaine = models.ManyToManyField(Domaine,null=True)
    def __str__(self) -> str:
        return self.name


class Reponse (models.Model):
    reponse = models.CharField(max_length=255)
    domaines = models.ManyToManyField(Domaine, null=True)
    point = models.IntegerField(default=10)
    def __str__(self) -> str:
        return self.reponse


class Question (models.Model):
    question = models.TextField()
    reponse = models.ManyToManyField(Reponse, null=True)
    def __str__(self) -> str:
        return self.question
