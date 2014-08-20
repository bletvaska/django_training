from django.test import TestCase
from pyper.models import Post, Tag
from django.contrib.auth.models import User
from django.test.client import Client
from django.core.urlresolvers import reverse

# Create your tests here.
class PostTests(TestCase):
    def setUp(self):
        author = User.objects.create(username='john')
        post = Post.objects.create(content='#hello #world from #django', author=author)

    def test_tags_recognition(self):
        author = User.objects.get(username='john')
        post = Post.objects.get(pk=1)

        for tag in post.tags.all():
            self.assertIn(tag.title, ('hello', 'world', 'django'))

    def test_form(self):
        client = Client()
        url = reverse('post_create')

        response = client.post(url, {'content': '#linksys router', 'author': 1})

        post = Post.objects.get(content='#linksys router')

        self.assertIsNotNone(post)

class RestAPITests(TestCase):
    def setUp(self):
        author = User.objects.create(username='john')
        post = Post.objects.create(content='#hello #world from #django', author=author)

    def test_all_posts(self):
        client = Client()
        url = reverse('post_rest_api')
        response = client.get(url)

        self.assertEqual(response.status_code, 200)

        self.assertEqual(len(response.data), 1)

        # response.context_data -> data as json
        # response.template_name -> name of the template to be rendered

