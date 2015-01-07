from django.conf.urls import patterns, url

from poem_gen import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index')
)