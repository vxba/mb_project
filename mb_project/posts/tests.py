from django.test import TestCase
from .models import Post
from django.urls import reverse

# Create your tests here.

class PostModelTesst(TestCase):
    def setUp(self):
        Post.objects.create(text='this is test')
    
    def testTestContent(self):
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name, 'this is test')

class HomePageViewTest(TestCase):
    def setUp(self):
        Post.objects.create(text = 'this is another test')
    
    def testViewUrlExistAtProperLocation(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def testViewUrlByName(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def testViewUserCorrectTemplate(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')

