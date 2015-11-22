from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.shortcuts import render
from apps.quiz.models import Question, Choice

def index(request):
	questions = Question.objects.all()

	context = {
		'questions': questions,
	}
	return render(request, 'quiz/index.html', context)

def show(request, question_id):

	req_question = Question.objects.get(id=question_id)

	choices = Choice.objects.all().filter(question=req_question)

	context = {
		'question' = question,
		'choices': choices,
	}
	return render(request, 'quiz/show.html', context)
	# if int(question_id) == 1:
	# 	return HttpResponse('<h1>Page found!</h1>')
	# else:
	# 	return HttpResponseNotFound('<h1> Page not found! </h1>')
	# return HttpResponse("You are looking at question number %s." % question_id)