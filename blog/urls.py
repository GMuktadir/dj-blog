from django.conf.urls import url
from blog import views


#blog sub Urls patterns
urlpatterns=[
		url(r'^time/$',views.today_is,name='todays_time'),
	#	url(r'^$',views.index,name='blog_index'),

]
