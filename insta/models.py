from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='images', null=True)


    image = CloudinaryField('image')
    image_name = models.CharField(max_length=50)
    image_caption = models.TextField(max_length=100)
    image_date = models.DateTimeField(auto_now_add=True)
    # profile = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    liked= models.ManyToManyField(User,default=None,blank=True,related_name='liked')
    comment_count = models.IntegerField(default=0,blank=True, null=True)
  
    @classmethod
    def get_images_by_user(cls, user):
        images = cls.objects.filter(user=user)
        return images

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    # update image text
    def update_caption(self, new_caption):
        self.image_caption = new_caption
        self.save()
    
    @classmethod
  # search images using image name
    def search_image_name(cls, search_term):
        images = cls.objects.filter(
        image_name__icontains=search_term)
        return images    

    def __str__(self):
        return self.user.username       

    def __str__(self):
        return self.image_name
    #  get a single image using id
    @classmethod
    def get_single_image(cls, id):
        image = cls.objects.get(id=id)
        return image

    def __str__(self):
        return self.image_name


    
    def __str__(self):
        return self.image_name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    profile_photo = CloudinaryField('image')

    bio = models.TextField(max_length=500, blank=True, null=True)

    contact = models.CharField(max_length=50, blank=True, null=True)

    def update(self):
        self.save()

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def get_profile_by_user(cls, user):
        profile = cls.objects.filter(user=user)
        return profile


LIKE_CHOICES={
    ('Like','Like'),
    ('Unlike','Unlike',)
}
class Likes(models.Model):
    image = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES,default='like',max_length=10)

    def str(self):
        return self.value
    
class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.CharField(max_length=500)
    comment_date = models.DateTimeField(auto_now_add=True)
    def save_comment(self):
        self.save()

    def __str__(self):
        return self.comment
