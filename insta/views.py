from django.shortcuts import render
from .models import *

from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    images = Post.objects.all().order_by('-id')
 
    return render(request, 'all-clone/index.html', {'images': images})