

# Create your tests here.

from django.test import TestCase
from .models import *

# test image class


class PostTestCase(TestCase):
    def setUp(self):
        # create a user
        user = User.objects.create(
            username='test_user',
            first_name='diana',
            last_name='mongina'
        )
        Post.objects.create(
            image_name='test_image',
            image='https://unsplash.com/photos/Pp6efQ_ghiA',
            image_caption='test image',
        )
    def test_image_name(self):
        image = Post.objects.get(image_name='test_image')
        self.assertEqual(image.image_name, 'test_image')

class ProfileTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(
            username='test_user',
            first_name='diana',
            last_name='mongina'
        )
        Profile.objects.create(
            bio='test bio',
            profile_photo='https://unsplash.com/photos/Pp6efQ_ghiA',
            user_id=user.id
        )

    def test_bio(self):
        profile = Profile.objects.get(bio='test bio')
        self.assertEqual(profile.bio, 'test bio')

