from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('titulo', 'subTitulo', 'owner', 'cuerpo')
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title for this post'}),
            'subTitulo': forms.TextInput(attrs={'class': 'form-control'}),
            'owner': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'usuario', 'type': 'hidden'}),
            'cuerpo': forms.Textarea(attrs={'class': 'form-control'}),
        }

class PostEditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('titulo', 'subTitulo', 'cuerpo')
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title for this post'}),
            'subTitulo': forms.TextInput(attrs={'class': 'form-control'}),
            'cuerpo': forms.Textarea(attrs={'class': 'form-control'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['commentOwner', 'post', 'texto']
        widgets = {
            'commentOwner': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'usuario', 'type': 'hidden'}),
            'post': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'post', 'type': 'hidden'}),
            'texto': forms.Textarea(attrs={'class': 'form-control'}),
        }


class BusquedaPostForm():
    nombre = forms.CharField(min_length=3, max_length=40)

class BusquedaCommentForm():
    nombre = forms.CharField(min_length=3, max_length=40)