from django.db import models


class Patient(models.Model):
    pesel = models.CharField(max_length=11)
    first_name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    age = models.IntegerField()

# ./manage.py loaddata data.json
