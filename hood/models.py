from __future__ import unicode_literals
from django.db import models
from tinymce.models import HTMLField
from cloudinary.models import CloudinaryField
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    profile_pic = CloudinaryField('image')
    bio = models.TextField(max_length=1000)
    about = models.TextField(max_length=5000)
    
    def __str__(self):
        return self.username

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

class Post(models.Model):
    title = models.CharField(max_length=500)
    image=CloudinaryField('image')
    description=models.TextField(max_length=2000)
    hood = models.ForeignKey('Hood', on_delete = models.CASCADE,default=None)
    business = models.ForeignKey('Business', on_delete = models.CASCADE,default=None)
    user = models.ForeignKey(User,on_delete = models.CASCADE)

    
    def save_post(self):
        self.save()

    def __str__(self):
        return self.hood

    @classmethod
    def all_posts(cls):
    
        all_posts = cls.objects.all()
        return all_posts

    @classmethod
    def one_post(cls,id):
        one_post = cls.objects.filter(id=id)
        return one_post

    @classmethod
    def user_posts(cls,user):
        user_posts = cls.objects.filter(user = user)
        return user_posts

    @classmethod
    def search_post(cls,search_term):
        searched_post = cls.objects.filter(title = search_term)
        return searched_post


class Hood(models.Model):
    name = models.CharField(max_length=500)
    

def save_hood(self):
        self.save()

def delete_hood(self):
        self.delete()

def __str__(self):
        return self.name

class Business(models.Model):
    name = models.CharField(max_length=500)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
def __str__(self):
        return self.name

def save_business(self):
        self.save()

def delete_business(self):
        self.delete()
# 
class Comment(models.Model):
    post_id = models.ForeignKey(Post,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    text = models.CharField(max_length=1000)

    # def __str__(self):
    #     return self.user


    @classmethod
    def get_all_comments(cls,id):
        comments = cls.objects.filter(post_id = id)
        return comments

    def save_comments(self):
        self.save()

    def delete_comment(self):
        self.delete()