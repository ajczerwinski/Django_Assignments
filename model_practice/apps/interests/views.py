from django.shortcuts import render
from django.http import HttpResponse, Http404
from apps.interests.models import User, Interest

# Create your views here.
def index(request):
	return render(request, 'interests/index.html')

def show(request):
	users = User.objects.all().select_related('interest')
	context = {
		"users": users,
	}
	return render(request, 'interests/show.html', context)

def show_user(request, user_id):
	user = User.objects.filter(id=user_id).select_related('interest')[0]
	context = {
		"user": user
	}
	return render(request, 'interests/show_user.html', context)
	