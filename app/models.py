from django.db import models

# Create your models here.
class Todos(models.Model):
    item = models.CharField(max_length=300)