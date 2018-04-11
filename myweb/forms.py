from django import forms
from .models import register

class Reg(forms.ModelForm):
    class Meta:
      model=register
      fields=('username','name','email','mobile','password','city',)


    '''
    username = forms.CharField(max_length=100)
    name = forms.CharField(max_length=100)
    email = forms.CharField(max_length=255)
    mobile = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    '''

