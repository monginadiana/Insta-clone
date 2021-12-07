

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
            image='https://doographics.com/assets/dg/images/cooking-youtube-thumbnail/cooking',
            image_caption='test image',
            profile_id=user.id,
            user_id=user.id
        )
    def test_image_name(self):
        image = Post.objects.get(image_name='test_image')
        self.assertEqual(image.image_name, 'test_image')


