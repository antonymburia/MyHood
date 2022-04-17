from django import forms
from django.contrib.auth.models import User
from .models import User,Profile,Comment,Post
from django.contrib.auth.forms import UserCreationForm

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['user','post_id']

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

