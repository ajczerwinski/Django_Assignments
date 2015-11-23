from django.shortcuts import render, render_to_response, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
	try:
		request.session['attempt']
	except:
		request.session['attempt'] = 0
	return render(request, 'random_word/index.html')

def randomize(request):
	request.session['my_string'] = get_random_string(length=14)
	# my_string = get_random_string(length=14)
	print request.session['my_string']
	# Un-comment the two lines below to clear the session
	# del request.session['my_string']
	# del request.session['attempt']
	request.session['attempt'] += 1
	return redirect('index')