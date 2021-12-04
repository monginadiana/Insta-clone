from django.contrib import admin

from insta.models import Post, Comments, Likes,  Profile

# Register your models here.
admin.site.register(Post)
admin.site.register(Comments)
admin.site.register(Likes)
admin.site.register(Profile)
