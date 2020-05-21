from django.shortcuts import render

# Create your views here.
def home_view(request):
	return render(request, 'testapp/home.html')

def movie_news_view(request):
	news1 = 'In Telugu Bahubali created created sensation'
	news2 = 'Prabhas done a fantastic job in bahubali'
	news3 = 'Good movie from Nani'
	my_dict = {'news1': news1, 'news2': news2, 'news3': news3}
	return render(request, 'testapp/movienews.html', my_dict)
