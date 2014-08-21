import re
from django.test import TestCase
from django.contrib.auth.models import User
from pyper.models import Post, Tag


class PostTests(TestCase):

    @classmethod
    def setUpClass(cls):
        print('--------------- running setup')

        content = '#django is #mega #super #bomba #spica'
        pattern = re.compile(r'#(?P<title>\w+)')
        cls.tags = pattern.findall(content)
        cls.non_tags = ('jano', 'cita', 'knihu')

        author = User.objects.create(username='tester')
        cls.post = Post.objects.create(
            content=content,
            author=author
        )

    def test_number_of_extracted_hashtags(self):
        # check number of tags
        self.assertTrue(len(self.post.tags.all()) == len(self.tags))


    def test_hashtags_extraction(self):
        # check if the post is of type Post
        self.assertIsInstance(type(self).post, Post)

        # test for all tags
        for tag in self.post.tags.all():
            self.assertIn(tag.title, self.tags)
            self.assertNotIn(tag.title, self.non_tags)

