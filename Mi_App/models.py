from django.db import models

class Familia (models.Model):
    miembro = models.CharField(max_length=20)
    edad = models.IntegerField()

class familia_paterna(models.Model):
    nombre = models.CharField(max_length=20)
    edad = models.IntegerField()
    miembro = models.CharField(max_length=20)