from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form_class-control', 'placeholder': 'Title for this post'}),
            'subTitulo': forms.TextInput(attrs={'class': 'form_class-control'}),
            'owner': forms.TextInput(
                attrs={'class': 'form_class-control', 'value': '', 'id': 'user', 'type': 'hidden'}),
            'cuerpo': forms.Textarea(attrs={'class': 'form_class-control'}),
        }


class PostEditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form_class-control', 'placeholder': 'Title for this post'}),
            'subTitulo': forms.TextInput(attrs={'class': 'form_class-control'}),
            'cuerpo': forms.Textarea(attrs={'class': 'form_class-control'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['commentOwner', 'post', 'texto']
        widgets = {
            'commentOwner': forms.TextInput(
                attrs={'class': 'form_class-control', 'value': '', 'id': 'user', 'type': 'hidden'}),
            'post': forms.TextInput(attrs={'class': 'form_class-control', 'value': '', 'id': 'post', 'type': 'hidden'}),
            'texto': forms.Textarea(attrs={'class': 'form_class-control'}),
        }


class BusquedaPostForm():
    nombre = forms.CharField(min_length=3, max_length=40)


class BusquedaCommentForm():
    nombre = forms.CharField(min_length=3, max_length=40)
