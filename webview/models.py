from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_missing = models.DateField(max_length=10)
    age_at_missing = models.IntegerField(max_length=3)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=2)
    gender = models.CharField(max_length=1)
    race = models.CharField(max_length=1)
