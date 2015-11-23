from django.conf.urls import include, url, patterns
from apps.surveys import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^result/', views.result, name='result'),
	url(r'^process_form/', views.process_form, name='process_form')
	)