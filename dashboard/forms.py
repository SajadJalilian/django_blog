from django import forms

from blog.models import Post


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image', 'categories']
