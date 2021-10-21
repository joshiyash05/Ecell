from django.db import models

# Create your models here.
class Student(models.Model):
	Name = models.CharField(max_length= 100)
	Sapid = models.CharField(max_length= 100)
	Branch = models.CharField(max_length= 100)
	contactno = models.CharField(max_length= 100)
	emailid = models.CharField(max_length= 100)