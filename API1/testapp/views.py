from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def emp_data_view(request):
	emp_data = {
		'eno': 100,
		'ename': 'Janardhan',
		'esal': 30000,
		'edept': 'DevOps',
	}
	resp = 'Employee Number:{}Employee Name:{}Employee Salary:{}Employee Department:{}'.format(emp_data['eno'],
																							   emp_data['ename'],
																							   emp_data['esal'],
																							   emp_data['edept'])
	return HttpResponse(resp)


import json


def emp_data_jsonview(request):
	emp_data = {
		'eno': 100,
		'ename': 'Janardhan',
		'esal': 30000,
		'edept': 'DevOps',
	}
	json_data = json.dumps(emp_data)
	return HttpResponse(json_data, content_type='application/json')


from django.http import JsonResponse


def emp_data_jsonview2(request):
	emp_data = {
		'eno': 100,
		'ename': 'Janardhan',
		'esal': 30000,
		'edept': 'Development',
	}
	return JsonResponse(emp_data)


from django.views.generic import View  ###  class based view


class JsonCBV(View):
	def get(self, request, *args, **kwargs):
		emp_data = {
			'eno': 100,
			'ename': 'Janardhan',
			'esal': 30000,
			'edept': 'Development',
		}
		return JsonResponse(emp_data)


from django.views.generic import View
from .mixins import HttpResponseMixin

class JsonCBV1(HttpResponseMixin,View):
	def get(self, request, *args, **kwargs):
		json_data = json.dumps({'msg': 'This is from get method'})
		return self.render_to_http_response(json_data)


	def post(self, request, *args, **kwargs):
		json_data = json.dumps({'msg': 'This is from post method'})
		return self.render_to_http_response(json_data)

	def put(self, request, *args, **kwargs):
		json_data = json.dumps({'msg': 'This is from put method'})
		return self.render_to_http_response(json_data)

	def delete(self, request, *args, **kwargs):
		json_data = json.dumps({'msg': 'This is from delete method'})
		return self.render_to_http_response(json_data)
