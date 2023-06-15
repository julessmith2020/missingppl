from django.contrib import admin
from .models import Person

# Register your models here.
#helps the admin site connect with the Person database table in order to add values and inputs from the creator's end

admin.site.register(Person)
