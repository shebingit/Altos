from django.db import models


class Courses(models.Model):
    course_name=models.CharField(max_length=40)
    course_discr=models.TextField()
    course_img=models.ImageField(upload_to="course/")

class OnProjects(models.Model):
    project_name=models.CharField(max_length=40)
    project_discr=models.TextField()
    project_img=models.ImageField(upload_to="project/")


class Clients(models.Model):
    client_name=models.CharField(max_length=40)
    client_discr=models.TextField()
    client_logo=models.ImageField(upload_to="client/")


class Enquery(models.Model):
    course_id=models.ForeignKey(Courses,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=60)
    email=models.EmailField()
    contact=models.CharField(max_length=15)
    place=models.CharField(max_length=20)

class Project_Enquery(models.Model):
    project_id=models.ForeignKey(OnProjects,on_delete=models.CASCADE,null=True,blank=True)
    enq_name=models.CharField(max_length=60)
    enq_email=models.EmailField()
    enq_contact=models.CharField(max_length=15)
    enq_project=models.CharField(max_length=40)
    enq_message=models.TextField()
