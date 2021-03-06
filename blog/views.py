from django.shortcuts import get_object_or_404, render, get_list_or_404
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import (
      ListView,
      DetailView, 
      CreateView,
      UpdateView,
      DeleteView
      )
from .models import Post


def home(request):
    context = {
       'posts': Post.objects.all()
      
    }
    return render(request,'blog/home.html',context)

# = /home
class PostListView(ListView):
      model = Post
      template_name = 'blog/home.html' #default path to view: <app>/<model>_<viewtype>.html  blog/post_list.html
      context_object_name = 'posts'
      ordering = ['-date_posted']
      paginate_by = 5



# = /home with user filter
class UserPostListView(ListView):
      model = Post
      template_name = 'blog/user_posts.html' #default path to view: <app>/<model>_<viewtype>.html  blog/post_list.html
      context_object_name = 'posts'
      paginate_by = 5

      def get_queryset(self):
            user = get_object_or_404(User,username=self.kwargs.get('username'))
            return Post.objects.filter(author=user).order_by('-date_posted')
      
class PostDetailView(DetailView):
      model = Post

# LoginRequiredMixin -- determ that user have to login
class PostCreateView(LoginRequiredMixin,CreateView):
      model = Post
      fields = ['title','content']
      
      # Set the author to the current login user
      def form_valid(self,form):
            form.instance.author = self.request.user
            return super().form_valid(form)

# LoginRequiredMixin -- determ that user have to login
# UserPassesTestMixin -- determ if login user pass test condition
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
      model = Post
      fields = ['title','content']
      
      # Set the author to the current login user
      def form_valid(self,form):
            form.instance.author = self.request.user
            return super().form_valid(form)

      # Test inf login user is the same as posted author. 
      def test_func(self):
          post = self.get_object()
          if self.request.user == post.author:
                return True
          return False      

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
      model = Post
      success_url = '/'
      
      # Test inf login user is the same as posted author. 
      def test_func(self):
          post = self.get_object()
          if self.request.user == post.author:
                return True
          return False     
    
def about(requst):
   return render(requst,'blog/about.html',{'title': 'About'})