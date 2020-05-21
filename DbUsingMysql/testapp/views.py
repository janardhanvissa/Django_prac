from django.shortcuts import render
from .models import employee


# Create your views here.
def index(request):
	return render(request, 'testapp/index.html')


def employee_views(request):
	employee_list = employee.objects.all()  # Employee------>model name
	return render(request, 'testapp/emp.html', {'employee_list': employee_list})
