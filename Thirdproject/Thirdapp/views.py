from django.shortcuts import render
import datetime


# Create your views here.


def template_view(request):
	dt = datetime.datetime.now()
	name = 'Janardhan'
	emp_id = 1321
	salary = 20000
	my_dict = {'date': dt, 'name': name, 'emp_id': emp_id, 'salary': salary}
	return render(request, 'Thirdapp/results.html', my_dict)
