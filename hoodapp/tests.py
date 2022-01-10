from django.test import TestCase
from .models import NeighborHood,Business,Post
from django.contrib.auth.models import User
# Create your tests here.
class TestNeighbour(TestCase):
    def setUp(self):
        self.new_hood=NeighborHood(name="Membley",location="Membley",occupationCount=20)
        self.new_business=Business(businessesName='Shoe it up',user=User(1),neighborhood=NeighborHood(1),email='@gmail.com')
        self.new_user=User(username='larvine')
        self.new_post=Post(image='img.png',post='liked',user=User(1),neighborhood=NeighborHood(0))
    def test_initialization(self):
        self.assertTrue(self.new_hood.name,'Membley')
        self.assertTrue(self.new_hood.location,'Membley')
        self.assertTrue(self.new_hood.occupationCount,20)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_hood,NeighborHood))

    def test_create_neighborhood(self):
        self.new_hood.create_neighborhood()
        hood=NeighborHood.objects.all()
        self.assertTrue(len(hood)>0)

    def test_delete_neighborhood(self):
        self.new_hood.delete_neighborhood()
        hood=NeighborHood.objects.all()
        self.assertEqual(len(hood),0)

    def test_find_neighborhood(self):
        self.new_hood.create_neighborhood()
        self.new_hood.find_neighborhood(1)
        hood=NeighborHood.objects.all()
        self.assertEqual(len(hood),1)


    def test_initialize(self):
        self.assertEqual(self.new_business.businessesName,'shoe it up')
        self.assertEqual(self.new_business.user,User(1))
        self.assertEqual(self.new_business.email,'@gmail.com')

    def test_instances(self):
        self.assertTrue(isinstance(self.new_business,Business))

    def test_create_business(self):
        self.new_user.save()
        self.new_hood.create_neighborhood()
        self.new_business.create_business()
        busines=Business.objects.all()
        self.assertTrue(len(busines)>0)

    def test_delete_business(self):
        self.new_business.delete_business()
        busines=Business.objects.all()
        self.assertTrue(len(busines)==0)

    def test_update_business(self):
        saved=Business.objects.filter(id=1)
        self.assertEqual(len(saved),0)


    def test_find_business(self):

        busines=Business.objects.all()
        self.assertTrue(len(busines)==0)

    def test_instanc(self):
        self.assertTrue(isinstance(self.new_post,Post))


    def test_correct_initialization(self):
        self.assertEqual(self.new_post.image,'img.png')
        self.assertEqual(self.new_post.user,User(1))
        self.assertEqual(self.new_post.neighborhood,NeighborHood(0))

    def test_post_save(self):
        self.new_user.save()
        self.new_hood.create_neighborhood()
        self.new_post.save_post()
        post=Post.objects.all()
        self.assertTrue(len(post)>0)
# class TearDown(TestCase):
#
#     def tearDown(self):
#         Businesses.objects.all().delete()
#         Feeds.objects.all().delete()
#         Neighbor.objects.all().delete()
#         User.objects.all().delete()Business,Post

