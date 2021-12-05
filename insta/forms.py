from django import forms
from django.db.models import fields
from insta.models import Post,Profile

class UpdateImageForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={

        'id': 'imageform', 'class': 'uploadimage'

    }))

    class Meta:
        model = Post
        fields = ['image','image_name','image_caption']