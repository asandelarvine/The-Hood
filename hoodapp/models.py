from django.db import models
import datetime as dt
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db.models.fields import TextField
from django.dispatch import receiver
from django.db.models.signals import post_save

from django.db.models import Q


# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=30)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    def save_location(self):
        self.save()
    def __str__(self):
        return self.name

class NeighborHood(models.Model):
    name = models.CharField(max_length=50)
    photo = CloudinaryField("image",null=True)
    content = models.TextField(max_length=600, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE,null=True)
    occupants_count = models.IntegerField(default=0)
    admin = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    created_on = models.DateTimeField(auto_now_add=True,null=True)
    updated_on = models.DateTimeField(auto_now=True,null=True)
    def create_neigborhood(self):
        self.save()
    @classmethod
    def delete_neighborhood(cls, id):
        cls.objects.filter(id=id).delete()
    @classmethod
    def update_neighborhood(cls, id):
        cls.objects.filter(id=id).update()
    @classmethod
    def search_by_name(cls, search_term):
        hood = cls.objects.filter(name__icontains=search_term)
        return hood
    @classmethod
    def find_neigborhood(cls, id):
        hood = cls.objects.get(id=id)
        return hood
    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile',null=True)
    profile_photo = CloudinaryField("image")
    bio = models.TextField(max_length=300)
    location = models.ForeignKey(Location, on_delete=models.CASCADE,null=True)
    neighborhood = models.ForeignKey(NeighborHood,related_name="members", on_delete=models.CASCADE,null=True)
    contact = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True,null=True)
    updated_on = models.DateTimeField(auto_now=True,null=True)


    def __str__(self):
        return f'{self.user.username} profile'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


# business class
class Business(models.Model):
     
    logo = CloudinaryField("image")
    content = models.TextField(max_length=600, null=True)
    neighborhood = models.ForeignKey(NeighborHood,on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name =models.CharField(max_length=100)
    email = models.EmailField()
    address =models.CharField(max_length=100)
    contact = models.IntegerField()

    
    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return f'{self.name} Business'

    def new_business(self):
        self.save()
    def update_business(self):
        self.update()
    @classmethod
    def delete_business(cls, id):
        cls.objects.filter(id=id).delete()
    @classmethod
    def update_business(cls, id):
        cls.objects.filter(id=id).update()
    @classmethod
    def search_by_name(cls, search_term):
        hood = cls.objects.filter(name__icontains=search_term)
        return hood
    @classmethod
    def find_business(cls, id):
        hood = cls.objects.get(id=id)
        return hood

    

    


# Authorities
class Authorities(models.Model):
    photo = CloudinaryField("image",null=True)
    neighborhood = models.ForeignKey(NeighborHood,on_delete=models.CASCADE)
    name =models.CharField(max_length=100)
    location = models.ForeignKey(Location, on_delete=models.CASCADE,null=True)
    content = models.TextField(max_length=600, null=True)
    email = models.EmailField()
    contact = models.IntegerField()
    address =models.CharField(max_length=100)


    def create_authorities(self):
        self.save()
    @classmethod
    def delete_authorities(cls, id):
        cls.objects.filter(id=id).delete()
    @classmethod
    def update_authorities(cls, id):
        cls.objects.filter(id=id).update()
    @classmethod
    def search_by_name(cls, search_term):
        hood = cls.objects.filter(name__icontains=search_term)
        return hood
    @classmethod
    def find_authorities(cls, id):
        hood = cls.objects.get(id=id)
        return hood

    def __str__(self):
        return self.name

# health
class Health(models.Model):
    logo = CloudinaryField("image",null=True)
    neighborhood = models.ForeignKey(NeighborHood,on_delete=models.CASCADE)
    name =models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.IntegerField()
    address =models.CharField(max_length=100)

    def create_health(self):
        self.save()

    def delete_health(self):
        self.delete()

    def update_health(self):
        self.update()
    

    def __str__(self):
        return self.name




class Category(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def create_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    def update_category(self):
        self.update()

    def __str__(self):
        return self.name


#Post model
class Post(models.Model):
    title = models.CharField(max_length=120, null=True)
    image=CloudinaryField('image',null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, null=True)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE,null=True)
    neighborhood = models.ForeignKey(NeighborHood, on_delete=models.CASCADE, related_name='hood_post',null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-pk']
        
    def __str__(self):
        return f'{self.title} Post'

    def create_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    def update_post(self):
        self.update()

    


# comment
class Comment(models.Model):
    comment = models.CharField(max_length=300)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)

