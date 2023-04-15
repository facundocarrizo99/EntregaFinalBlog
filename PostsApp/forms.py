from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['fecha', 'foto']
        #fields = ['__all__']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['fecha']
        #fields = ['texto', 'commentOwner', 'post']


class BusquedaPostForm():
    nombre = forms.CharField(min_length=3, max_length=40)

class BusquedaCommentForm():
    nombre = forms.CharField(min_length=3, max_length=40)