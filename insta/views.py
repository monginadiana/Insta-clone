from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from .forms import UpdateImageForm
import cloudinary
import cloudinary.uploader
import cloudinary.api

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    images = Post.objects.all().order_by('-id')
    users= User.objects.exclude(id=request.user.id)
    
 
    return render(request, 'all-clone/index.html', {'images': images, 'users':users})

# @login_required(login_url='/accounts/login/')
# def post(request):
#     if request.method == 'POST':
#         image_name = request.POST['image_name']
#         image_caption = request.POST['image_caption']
#         image_file = request.FILES['image_file']
#         image_file = cloudinary.uploader.upload(image_file)
#         image_url = image_file['url']
#         image = Post(image_name=image_name, image_caption=image_caption, image=image_url,
#                       profile_id=request.POST['user_id'], user_id=request.POST['user_id'])
#         image.save_image()
#         return redirect('/profile', {'success': 'Successfully posted'})
#     else:
#         return render(request, 'all-clone/profile.html', {'danger': 'posting Failed'})

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    images = Post.objects.filter(user_id=current_user.id)
    profile = Profile.objects.filter(user_id=current_user.id).first()
    form = UpdateImageForm()
    if request.method == 'POST':
        form = UpdateImageForm (request.POST , request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
        redirect('all-clone/profile')
    return render(request, 'all-clone/profile.html', {"images": images, "profile": profile, "form": form})
 
def like_image(request):
    user = request.user
    if request.method == 'POST':
        image_id = request.POST.get('image_id')
        image_pic =Post.objects.get(id=image_id)
        if user in image_pic.liked.all():
            image_pic.liked.add(user)
        else:
            image_pic.liked.add(user)    
            
        like,created =Likes.objects.get_or_create(user=user, image_id=image_id)
        if not created:
            if like.value =='Like':
               like.value = 'Unlike'
        else:
               like.value = 'Like'

        like.save()       
    return redirect('index')


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

def image(request,image_id):
    try:
        images = Post.objects.get(id = image_id)
    except ObjectDoesNotExist:
        raise Http404()
    return render(request,"all-clone/Image.html", {"images":images})



