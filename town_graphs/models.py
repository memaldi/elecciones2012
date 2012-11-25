from django.db import models

# Create your models here.

class Provincia(models.Model):
    #cod = models.IntegerField()
    name = models.CharField(max_length=50)
    
class Municipio(models.Model):
    #cod = models.IntegerField()
    name = models.CharField(max_length=50)
    provincia = models.ForeignKey(Provincia)
    censo = models.IntegerField()
    nulos = models.IntegerField()
    blancos = models.IntegerField()
    candidatos = models.IntegerField()
    abstenciones = models.IntegerField()
    lat = models.FloatField(null=True)
    long = models.FloatField(null=True)

class Partido(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=10)
    
class Votos(models.Model):
    partido = models.ForeignKey(Partido)
    municipio = models.ForeignKey(Municipio)
    num_votos = models.IntegerField(null=True)
