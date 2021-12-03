from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
import cloudinary
import cloudinary.uploader
import cloudinary.api

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    images = Post.objects.all().order_by('-id')
 
    return render(request, 'all-clone/index.html', {'images': images})

@login_required(login_url='/accounts/login/')
def post(request):
    if request.method == 'POST':
        image_name = request.POST['image_name']
        image_caption = request.POST['image_caption']
        image_file = request.FILES['image_file']
        image_file = cloudinary.uploader.upload(image_file)
        image_url = image_file['url']
        image = Post(image_name=image_name, image_caption=image_caption, image=image_url,
                      profile_id=request.POST['user_id'], user_id=request.POST['user_id'])
        image.save_image()
        return redirect('/profile', {'success': 'Successfully posted'})
    else:
        return render(request, 'profile.html', {'danger': 'posting Failed'})

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    images = Post.objects.filter(user_id=current_user.id)
    profile = Profile.objects.filter(user_id=current_user.id).first()
    return render(request, 'profile.html', {"images": images, "profile": profile})
