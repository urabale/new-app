from django import forms
from django.forms import fields
from .models import post
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class UserCreateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #htmlの表示を変更可能にします
        self.fields['username'].widget.attrs['class'] = 'form-group'
        self.fields['password1'].widget.attrs['class'] = 'form-group'
        self.fields['password2'].widget.attrs['class'] = 'form-group'

    class Meta:
       model = User
       fields = ("username", "password1", "password2",)

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = post
        fields = '__all__'