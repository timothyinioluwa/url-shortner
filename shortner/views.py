from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from .models import URL
import uuid
# Create your views here.
class HomeView(TemplateView):
    template_name = "home.html"
    
def create_link(request,*args, **kwargs):
    if request.method == 'POST':
        link = request.POST.get('link')
        uid = str(uuid.uuid4())[:5]
        new_url =URL(link=link,uuid=uid)
        new_url.save()
        return HttpResponse(uid)

def go_to_page(request,pk):
    urldetails = URL.objects.get(uuid=pk)
    return redirect(urldetails.link)