from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class Item(models.Model):
    name=models.CharField(max_length=30)
    detail=models.CharField(max_length=100)

    def _str_(self):
        return self.title
