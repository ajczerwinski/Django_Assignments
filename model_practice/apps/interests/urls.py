from django.conf.urls import patterns, url
from apps.interests import views
urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^interests/', views.show, name='interests'),
	url(r'^users/(?P<user_id>\d+)/$', views.show_user, name='show')

)