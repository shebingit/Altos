from django.db import models

class Enquery(models.Model):
    name=models.CharField(max_length=60)
    email=models.EmailField()
    contact=models.CharField(max_length=15)
    place=models.CharField(max_length=20)

class Project_Enquery(models.Model):
    enq_name=models.CharField(max_length=60)
    enq_email=models.EmailField()
    enq_contact=models.CharField(max_length=15)
    enq_project=models.CharField(max_length=40)
    enq_message=models.TextField()
