from django import forms
from .models import UserInfo
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your models here.


class ExtendUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    class Meta:
        model = User  
        fields =('first_name','last_name','email','username','password1','password2')


class UserInfoForm(forms.ModelForm):
    
    class Meta:
        model = UserInfo
        fields = ("phone_number","profile",)