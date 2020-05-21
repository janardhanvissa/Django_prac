from django.db import models


# Create your models here.
class employee(models.Model):
	name = models.CharField(max_length=30)
	dob = models.DateField()
	sal = models.IntegerField()
	email = models.EmailField()
	phone = models.IntegerField()
	addr = models.TextField()
