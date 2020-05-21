from django.shortcuts import render
import datetime


# Create your views here.
def date_time_view(request):
	date = datetime.datetime.now()
	h = int(date.strftime('%H'))
	if h<12 :
		msg='Hello Janardhan!!!! Very Good orning!!!'
	elif h<16:
		msg = 'Hello Janardhan!!!! Very Good Afternoon!!!'
	elif h<21:
		msg = 'Hello Janardhan!!!! Very Good Evening!!!'
	else:
		msg = 'Hello Janardhan!!!! Good Night!!!'

	my_dict = {'date':date, 'msg': msg}
	return render(request, 'testapp/results.html',my_dict)

