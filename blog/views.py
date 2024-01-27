from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
#listview is class ased view
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView, 
    UpdateView,
    DeleteView)
from .models import Post

# adding dummy data
# posts=[
#     {
#         'author': 'Kuhoo',
#         'title': 'Blog Post-1',
#         'content': 'Welcome to Kuhoo Interns',
#         'date_posted': 'January 8, 2024'
#     },
#     {
#         'author': 'Vedant Modi',
#         'title': 'Blog Post-2',
#         'content': 'B.Tech from NU-CSE 2024 in Tech Team Intern',
#         'date_posted': 'January 8, 2024'
#     }
# ]

#using post model to get data from database


#home function to handle traffic from homepage
def home(request):
    #context dictionary for the data dictionary
    context = {
        'posts': Post.objects.all(),
        'title': 'Blog Home Page'
    }
    return render(request, 'blog/home.html', context)
    # return render(request, 'blog/home.html', context) context --> how we want to pass information

def about(request):
    context = {
        'title': 'Blog About Page'
    }
    return render(request, 'blog/about.html', context)

#class of post view in listview class based component
class PostListView(ListView):
    model = Post
    #<app>/<model>_<viewtype>.html
    template_name='blog/home.html'
    context_object_name = 'posts' #that is what appearing in home page
    ordering=['-date_posted']
    paginate_by = 4
    
class UserPostListView(ListView):
    model = Post
    #<app>/<model>_<viewtype>.html
    template_name='blog/user_home.html'
    context_object_name = 'posts'
    paginate_by=4
    def get_query_set(self):
        user=get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author= self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False
    def form_valid(self, form):
        form.instance.author= self.request.user
        return super().form_valid(form)
    
class PostDeletView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False
