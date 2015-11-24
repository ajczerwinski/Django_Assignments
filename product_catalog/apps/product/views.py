from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from apps.product.models import Manufacturer, Product
from django.utils import timezone
# Create your views here.

def index(request):
	products = Product.objects.all().select_related('manufacturer')
	context = {
		'products':products,
	}
	return render(request, 'product/index.html', context)

def show(request, product_id):
	product = Product.objects.get(id=product_id)
	context = {
		'product':product,
	}
	print product.name
	print "DSFOJSPFOIJWPEOFIJWPEOFIJWEPOFIJ"
	return render(request, 'product/show.html', context)

def create(request):
	insert = Product(name=request.POST['name'], price=request.POST['price'], created_at=timezone.now(), manufacturer=Manufacturer.objects.get(name=request.POST['manu_name']), description=request.POST['description'])
	print insert
	insert.save()
	return redirect('/')

def update(request, product_id):
	update=Product.objects.get(id=product_id).update(name=request.POST['name'], price=request.POST['price'], created_at=timezone.now(), manufacturer=Manufacturer.objects.get(name=request.POST['manu_name']), description=request.POST['description'])
	context = {
		'product':update
	}
	return render(request, 'product/index.html', context)
def delete(request, product_id):
	Product.objects.get(id=product_id).delete()
	return redirect('/')