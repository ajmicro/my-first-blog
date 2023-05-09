from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('account_officer', 'address', 'text', 'post_image')
        
