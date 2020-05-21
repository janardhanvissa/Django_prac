from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def html_head(request):
	return HttpResponse('<h1>This is second app function calling</h1>')
