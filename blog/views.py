from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from . import views

posts = [
    {
        'author': 'CoryMs',
        'title': 'Blog Post1',
        'content': 'First post content',
        'date_posted': 'August 27, 2019'
    },
      {
        'author': 'CoryMs2',
        'title': 'Blog Post2',
        'content': 'Second post content',
        'date_posted': 'October 27, 2020'
    }
]



def home(request):
    context = {
        'posts': posts,
        'title': 'killer'
    }
    return render(request,'blog/home.html',context)

def about(requst):
   return render(requst,'blog/about.html',{'title': 'About'})