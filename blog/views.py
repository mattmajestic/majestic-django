from django.shortcuts import render
from .models import Post

def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'templates/home.html', context)

def blog(request):
    return render(request, 'templates/about.html')