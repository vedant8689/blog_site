from django.urls import path
from .views import (
    PostDetailView, 
    PostListView, 
    PostCreateView, 
    PostUpdateView,
    PostDeletView,
    UserPostListView)
#importing the view module in file
from . import views

#mapping url
urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeletView.as_view(), name='post-delete'),
    path('user/<str:username>', UserPostListView.as_view( ), name='user-post'),
    path('about/', views.about, name='blog-about'),
    
]

#<app>/<model>_<viewtype>.html