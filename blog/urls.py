from django.conf.urls import  url
#from blog import views
from . import views

#blog sub Urls patterns
urlpatterns=[
		url(r'^time/$',views.today_is,name='todays_time'),
		url(r'^list/$', views.post_list, name='post_list'),
	#url(r'^$',views.index,name='blog_index'),

]
