from django.conf.urls import include, url, patterns
from apps.ninja import views

urlpatterns = patterns('',
    url(r'^$', views.index, name = 'index'),
    #?P says: expect something
    # \w says: expect some letters
    # <color> is the name of variable that is going to be passed to show
    # w+ = more than 1 character!
    url(r'^(?P<color>\w+)/', views.show, name = 'show'),
)