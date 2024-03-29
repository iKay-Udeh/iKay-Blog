from django.views.generic import (
    ListView,
    DetailView,
)

from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView,
)

from django.urls import reverse_lazy

from .models import Post, Comment

from django.contrib.auth.models import User

# Create your views here.
class HomePageView(ListView):
    model= Post
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']

class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

class AddNewComment(CreateView):
    model = Comment
    template_name = 'add_comment.html'
    fields = ['name', 'body', 'post']
    success_url = reverse_lazy('home')


