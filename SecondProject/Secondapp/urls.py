from django.conf.urls import url
from . import views

urlpatterns = [
	url('first/', views.first_view),
	url('second/', views.second_view),
	url('third/', views.third_view),
	url('fourth/', views.fourth_view),
	url('fifth/', views.fifth_view),
]
