from django.db import models
from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Post(models.Model):
  

    image = CloudinaryField('image')
    image_name = models.CharField(max_length=50)
    image_caption = models.TextField(max_length=100)
    image_date = models.DateTimeField(auto_now_add=True)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    # update image text
    def update_caption(self, new_caption):
        self.image_caption = new_caption
        self.save()
    
    def __str__(self):
        return self.image_name