from django import forms

from .models import blog

class PostForm(forms.ModelForm):
    class Meta:
        model = blog
        fields = ('blogpost',)

