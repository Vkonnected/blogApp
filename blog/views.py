from django.shortcuts import render,get_object_or_404
#from django.http import HttpResponse
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.mixins import UserPassesTestMixin,LoginRequiredMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
# Create your views here.

def home(request):
    #return HttpResponse("<h1> Home Page </h1>")
    context={
        'posts':Post.objects.all()
    }
    return render(request,"blog/home.html",context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  #blog/post_list.html  (appname/model_viewtype.html)
    context_object_name = 'posts'
    ordering = ['-time']
    paginate_by = 2

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  #blog/post_list.html  (appname/model_viewtype.html)
    context_object_name = 'posts'
    ordering = ['-time']
    paginate_by = 2

    def get_queryset(self):
        user=get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-time')

class PostDetailView(LoginRequiredMixin,DetailView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)

    def test_func(self):
        post=self.get_object()
        if(post.author==self.request.user):
            return True
        else:
            return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post=self.get_object()
        if(post.author==self.request.user):
            return True
        else:
            return False


def about(request):
    #return HttpResponse ("<h1> About Page </h1>")
    return render(request, "blog/about.html",{'title':"about"})