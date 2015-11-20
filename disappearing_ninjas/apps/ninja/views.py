from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'ninja/index.html')
def show(request, color):
    context = {'color': color }
    return render(request, 'ninja/show.html', context)