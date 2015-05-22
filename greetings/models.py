from django.db import models

# Create your models here.

# passing models.Model to a new class declaration will extend that class
class Greeting(models.Model):
    text = models.CharField(max_length=20)
    language = models.CharField(max_length=5)

# by default, db.sqlite3 is the database for Django projects