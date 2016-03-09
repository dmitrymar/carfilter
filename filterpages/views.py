from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

# Create your views here.
# example url: http://localhost:8000/
def index(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'filterpages/index.html', {'posts': posts})

# example url: http://localhost:8000/post/1/
def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'filterpages/detail.html', {'post': post})

# example url: http://localhost:8000/overview/2016/honda/accord/coupe/
def overview(request, year, make, model, body=None):
    return render(request, 'filterpages/overview.html')
