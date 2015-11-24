from django.conf.urls import patterns, url, include
from apps.product import views
urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^products/(?P<product_id>\d+)/$', views.show, name='show'),
	url(r'^delete/(?P<product_id>\d+)/$', views.delete, name='delete'),
	url(r'^create', views.create, name='create'),
	url(r'^update/(?P<product_id>\d+)/$', views.update, name='update'),
)