from django.test import TestCase

from django.test import TestCase
from .models import NeighborHood,Post
from django.contrib.auth.models import User
import datetime as dt



# Create your tests here.
class neighbourhoodTestClass(TestCase):
    def setUp(self):
        self.Greenpark = NeighborHood(neighbourhood='Greenpark')

    def test_instance(self):
        self.assertTrue(isinstance(self.Greenpark,NeighborHood))

    def tearDown(self):
        NeighborHood.objects.all().delete()

    def test_save_method(self):
        self.Greenpark.save_neighbourhood()
        hood = NeighborHood.objects.all()
        self.assertTrue(len(hood)>0)

    def test_delete_method(self):
        self.Greenpark.delete_neighbourhood('Greenpark')
        hood = NeighborHood.objects.all()
        self.assertTrue(len(hood)==0)

class PostTestClass(TestCase):
    def setUp(self):
        self.Munch = Post(munch='Munch')

    def test_instance(self):
        self.assertTrue(isinstance(self.Munch))

    def tearDown(self):
        Post.objects.all().delete()

    def test_save_method(self):
        self.Munch.save_munch()
        rest = Post.objects.all()
        self.assertTrue(len(rest)>0)

    def test_delete_method(self):
        self.Munch.delete_munch('Munch')
        rest = Post.objects.all()
        self.assertTrue(len(rest)==0)