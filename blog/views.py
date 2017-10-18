#from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
import datetime
from django.utils import timezone
from .models import Post
# Create your views here.

def post_list(request):
    posts = Post.objects.all()
   #posts = Post.objects.get(pk=4)
    return render(request, 'blog/in.html', {'posts': posts})

def today_is(request):
    now = datetime.datetime.now()
    return render(request, 'blog/datetime.html',{'now': now})


def single_post(request,post_id):
   s_posts = Post.objects.get(pk=post_id)
   #print(s_posts)
   return render(request, 'blog/single_post.html',{'posts':s_posts})


def index(request):
	post=Post.objects.all()
	return render(request,'blog/index.html',{'post':index})



