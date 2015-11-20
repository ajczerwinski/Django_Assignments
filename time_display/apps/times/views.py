from django.shortcuts import render
from time import strftime
current_date = strftime('%b %-d, %Y')
# date = datetime.now(tz=pytz.utc)
# date = date.astimezone(timezone('US/Pacific'))
current_time = strftime('%I:%M %p')

# Create your views here.
def index(request):
	context = {
		'date': current_date,
		'time': current_time,
	}
	return render(request, 'times/index.html', context)