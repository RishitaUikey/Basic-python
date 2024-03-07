from django.db import models

# Create your models here.

class db_one(models.Model): # table_name
    #attributes
    name = models.CharField(max_length = 50)
    email = models.EmailField()
