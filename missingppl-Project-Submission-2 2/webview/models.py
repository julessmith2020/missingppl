from django.db import models

# Create your models here.
# we created a table Person with these values that will be inputed into the table as attributes (columns)
# the admin interface will then access this class to allow the admin user to input values into the fields
class Person(models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  date_missing = models.DateField()
  age_at_missing = models.IntegerField()
  city = models.CharField(max_length=20)
  state = models.CharField(max_length=2)
  gender = models.CharField(max_length=1)
  race = models.CharField(max_length=1)
