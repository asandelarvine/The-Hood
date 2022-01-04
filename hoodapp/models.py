from django.db import models
import datetime as dt
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db.models.fields import TextField

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
