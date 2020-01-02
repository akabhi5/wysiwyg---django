from django.shortcuts import render
from .models import Post
from .forms import PostForm

def post_view(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'post.html', {'post': post})

def add_post(request):
    form = PostForm()
    return render(request, 'add_post.html', {'form': form})
