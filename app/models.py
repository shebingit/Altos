from django.db import models

class Enquery(models.Model):
    name=models.CharField(max_length=60)
    email=models.EmailField()
    contact=models.CharField(max_length=15)
    place=models.CharField(max_length=20)
