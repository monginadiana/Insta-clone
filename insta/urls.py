from django.conf.urls import url
from django.contrib import admin
from insta import views


urlpatterns = [
    url(r'^$',views.index,name= 'index'),
    url("profile/", views.profile),
    # url('like/<int:id>/', views.like_image, name='like.image'),
    # url('comment/', views.save_comment, name='comment.add'),

]