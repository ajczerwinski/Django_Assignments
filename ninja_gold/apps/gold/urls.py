from django.conf.urls import include, url, patterns
from apps.gold import views

urlpatterns = patterns('',
	url(r'^process_money/', views.process_money, name='process_money'),
	url(r'^$', views.index, name='index')
	)