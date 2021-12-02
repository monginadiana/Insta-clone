from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    images = Post.objects.all().order_by('-id')
 
    return render(request, 'index.html', {'images': images})