import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DbUsingMySql.settings')
import django
django.setup()

from .models import *
from faker import Faker
from random import *
fake = Faker()


def phonenumbergen():
	d1 = randint(6, 9)
	num = '' + str(d1)
	for i in range(9):
		num = num + str(randint(0, 9))
	return int(num)


def populate(n):
	for i in range(n):
		fname = fake.name()
		fdob = fake.dob()
		fsal = fake.sal()
		femail = fake.email()
		fphonenumbergen = phonenumbergen()
		faddr = fake.random_element(
			elements=('Vijayawada', 'Guntur', 'Hyderabad' 'Chennai', 'Mumbai', 'Bangalore', 'Vizag'))
		employee_record = employee.objects.create(name=fname, dob=fdob, sal=fsal, email=femail,
												  phonenumbergen=fphonenumbergen, addr=faddr)


populate(30)
