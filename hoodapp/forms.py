from django.db.models import fields
from .models import  Profile, NeighborHood, Business, Authorities, Post, Comment
from django.forms import ModelForm
from django import forms


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'profile_photo','contact','location','neighborhood')

class HoodForm(forms.ModelForm):
    class Meta:
        model=NeighborHood
        fields = ['photo','name','content','occupants_count','location']

class BusinessForm(forms.ModelForm):
    class Meta:
        model=Business
        fields = ['logo','content','neighborhood','location','name','email','address','contact']

class AuthoritiesForm(forms.ModelForm):
    class Meta:
        model=Authorities
        fields = ['photo','neighborhood','name','location','content','email','contact','address']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('user', 'location')

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        exclude=['username','post']