from django.shortcuts import render, render_to_response, redirect
from django.utils.crypto import get_random_string
import random
import string
from datetime import datetime
output = ""
from time import strftime
time = strftime("%Y/%m/%d %I:%M %p")


# Create your views here.
def index(request):
	try:
		request.session['gold']
	except:
		request.session['gold'] = 0
	try:
		request.session['message']
	except:
		request.session['message'] = []

	return render(request, 'gold/index.html')

def process_money(request):
	# if "Farm" in request.POST:
	if request.POST['building'] == "Farm":
		request.session['farm_gold'] = random.randrange(10, 21)
		request.session['gold'] += request.session['farm_gold']
		output = "earned %d gold from the farm! (%s)" %(request.session['farm_gold'], time)
		request.session['message'].append(output)
		request.session['building'] = "Farm"
	# elif "Cave" in request.POST:
	elif request.POST['building'] == "Cave":
		request.session['cave_gold'] = random.randrange(5, 11)
		request.session['gold'] += request.session['cave_gold']
		output = "earned %d gold from the cave! (%s)" %(request.session['cave_gold'], time)
		request.session['message'].append(output)
		request.session['building'] = "Cave"
	# elif "House" in request.POST:
	elif request.POST['building'] == "House":
		request.session['house_gold'] = random.randrange(2, 6)
		request.session['gold'] += request.session['house_gold']
		output = "earned %d gold from the house! (%s)" %(request.session['house_gold'], time)
		request.session['message'].append(output)
		request.session['building'] = "House"
	# elif "Casino" in request.POST:
	elif request.POST['building'] == "Casino":
		request.session['ladyluck'] = random.randrange(1, 101)
		request.session['casino_gold'] = random.randrange(0, 51)
		if request.session['ladyluck'] > 50:
			request.session['gold'] += request.session['casino_gold']
			output = "Earned %d gold from the casino! (%s)" %(request.session['casino_gold'], time)
			request.session['message'].append(output)
		else:
			request.session['gold'] -= request.session['casino_gold']
			output = "Entered a casino and lost %d gold...Ouch! (%s)" %(request.session['casino_gold'], time)
			request.session['message'].append(output)
			request.session['building'] = "Casino"
	return redirect('index')