
from django.contrib import admin
from django.urls import path
#from .views import home
from . import views
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView

urlpatterns = [
    #path('', views.home,name="blog-home"),
    path('post/<int:pk>', PostDetailView.as_view(), name="post-detail"),
    path('post/<str:username>', UserPostListView.as_view(), name="user-posts"),
    path('post/new', PostCreateView.as_view(), name="post-create"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name="post-update"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="post-delete"),
    path('', PostListView.as_view(),name="blog-home"),
    path('about/', views.about,name="blog-about")
]
