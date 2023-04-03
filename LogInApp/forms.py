from django import forms
from .models import Admin, Blogger

class BloggerForm(forms.ModelForm):
    class Meta:
        model = Blogger
        fields = '__all__'

class AdminForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = '__all__'