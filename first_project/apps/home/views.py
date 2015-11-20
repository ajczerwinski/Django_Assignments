from django.shortcuts import render

# Create your views here.
def index(request):
	context = {
		'users': [
			{ 'content': 'My name is Michael Choi'},
			{ 'content': 'I like to play Basketball'},
			{ 'content': 'My favorite programming language is Python'},
		]
	}
	return render(request, 'home/index.html', context)