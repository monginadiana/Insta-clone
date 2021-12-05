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
        return render(request, 'all-clone/profile.html', {'danger': 'posting Failed'})

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    images = Post.objects.filter(user_id=current_user.id)
    profile = Profile.objects.filter(user_id=current_user.id).first()
    return render(request, 'all-clone/profile.html', {"images": images, "profile": profile})
 
@login_required(login_url='/accounts/login/')
def like_image(request, id):
    likes = Likes.objects.filter(image_id=id).first()
    # check if the user has already liked the image
    if Likes.objects.filter(image_id=id, user_id=request.user.id).exists():
        likes.delete()
        image = Post.objects.get(id=id)
        if image.like_count == 0:
            image.like_count = 0
            image.save()
        else:
            image.like_count -= 1
            image.save()
        return redirect('/')
    else:
        likes = Likes(image_id=id, user_id=request.user.id)
        likes.save()
        image = Post.objects.get(id=id)
        image.like_count = image.like_count + 1
        image.save()
        return redirect('/')


# @login_required(login_url='/accounts/login/')
# def save_comment(request):
#     if request.method == 'POST':
#         comment = request.POST['comment']
#         image_id = request.POST['image_id']
#         image = Post.objects.get(id=image_id)
#         user = request.user
#         comment = Comments(comment=comment, image_id=image_id, user_id=user.id)
#         comment.save_comment()
#         image.comment_count = image.comment_count + 1
#         image.save()
#         return redirect('/')
#     else:
#         return redirect('/')   

# 

@login_required(login_url='/accounts/login/')
def search_post(request):
    if 'search' in request.GET and request.GET['search']:
        search_term = request.GET.get('search').lower()
        images = Post.search_image_name(search_term)
        message = f'{search_term}'

        return render(request, 'all-clone/search.html', {'found': message, 'images': images})
    else:
        message = 'Not found'
        return render(request, 'all-clone/search.html', {'danger': message})