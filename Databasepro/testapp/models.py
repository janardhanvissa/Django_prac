from django.db import models

# Create your models here.
class Employee(models.Model):
	eno = models.IntegerField()
	ename = models.CharField(max_length=64)
	esal = models.FloatField()
	eaddr = models.CharField(max_length=255)

	def __str__(self):        #is to display ename when we click on Employee class in Admin interface
		return self.ename

