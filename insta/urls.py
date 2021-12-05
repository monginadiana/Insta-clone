from django.conf.urls import url
from django.contrib import admin
from insta import views


urlpatterns = [
    url(r'^$',views.index,name= 'index'),
    url(r'^profile/$', views.profile),
    url(r'^search/$', views.search_post, name='search.post')
    # url(r'like/<int:id>/ $', views.like_image, name='like.image'),
    # url('comment/', views.save_comment, name='comment.add'),

]