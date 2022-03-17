from multiprocessing import context
from re import template
from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Post


def home(request):
    context = {
       'posts': Post.objects.all()
      
    }
    return render(request,'blog/home.html',context)


class PostListView(ListView):
      model = Post
      template_name = 'blog/home.html' #default path to view: <app>/<model>_<viewtype>.html  blog/post_list.html
      context_object_name = 'posts'
      ordering = ['-date_posted']


class PostDetailView(DetailView):
      model = Post
      

def about(requst):
   return render(requst,'blog/about.html',{'title': 'About'})