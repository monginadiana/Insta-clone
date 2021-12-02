from django.shortcuts import render
from .models import Post

# Create your views here.

def home(request):
    images = Post.objects.all().order_by('-id')
 
    return render(request, 'index.html', {'images': images})