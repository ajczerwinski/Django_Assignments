from django.conf.urls import include, url, patterns
from apps.random_word import views

urlpatterns = patterns('',
	url(r'^random/', views.randomize, name='random_word'),
	url(r'^$', views.index, name='index')

	)