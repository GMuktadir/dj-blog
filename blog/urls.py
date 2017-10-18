from django.conf.urls import  url
from django.conf import settings
from django.conf.urls.static import static
#from blog import views
from . import views

#blog sub Urls patterns
urlpatterns=[
		url(r'^time/$',views.today_is,name='now'),
		url(r'^list/$', views.post_list, name='post_list'),
		url(r'^single_post/(?P<post_id>[0-9]+)/$', views.single_post, name='single_post'),
	    url(r'^$',views.index,name='index')
	    

]


