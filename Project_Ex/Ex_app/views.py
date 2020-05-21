from django.shortcuts import render
from django.http import HttpResponse
import datetime


# Create your views here.
def date_time_view(request):
	date = datetime.datetime.now()
	s = '<h1>This will shows the current date and time:' + str(date) + '</h1>'
	return HttpResponse(s)
