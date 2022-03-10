from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from . import views
from .models import Post


def home(request):
    context = {
       'posts': Post.objects.all()
      
    }
    return render(request,'blog/home.html',context)

def about(requst):
   return render(requst,'blog/about.html',{'title': 'About'})