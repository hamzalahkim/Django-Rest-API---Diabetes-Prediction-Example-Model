from django.db import models

# Create your models here.

class Patient(models.Model):
    name = models.TextField()
    pregnancies =  models.IntegerField()
    glucose =  models.FloatField()
    bloodpressure = models.FloatField()
    skinthickness = models.FloatField()
    insulin = models.FloatField()
    bmi = models.FloatField()
    diabetespedigree = models.FloatField()
    age = models.IntegerField()
    diagnosis = models.BooleanField(default=False)



