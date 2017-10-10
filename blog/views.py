from django.shortcuts import render
#from django.shortcuts import render_to_response
from django.conf import settings
#from django.http import HttpResponse
import datetime
# Create your views here.
#def index(request):
 #   return HttpResponse("Hello Jakir Hossain Welcome")

def today_is(request):
    now = datetime.datetime.now()
    return render(request, 'blog/datetime.html',
                  {'now': now,
                   'template_name': 'blog/nav.html',
                   'base_dir': settings.BASE_DIR}
                  )
def post_list(request):
    return render(request, 'blog/post_list.html', {})