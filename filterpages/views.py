from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .models import Carmodel

# Create your views here.
# example url: http://localhost:8000/
def index(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    carmodels = Carmodel.objects.all()
    return render(request, 'filterpages/index.html', {'posts': posts, 'carmodels': carmodels})

# example url: http://localhost:8000/post/1/
def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'filterpages/detail.html', {'post': post})

def test(request, pk):
    carmodel = get_object_or_404(Carmodel, pk=pk)
    return render(request, 'filterpages/test.html', {'carmodel': carmodel})

# example url: http://localhost:8000/overview/2016/honda/accord/coupe/
def overview(request, year, make, model, body=None, version=None):
    carmodel = get_object_or_404(Carmodel, make=make)
    return render(request, 'filterpages/overview.html', {'carmodel': carmodel})
