import re
import logging
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

logger = logging.getLogger(__name__)


class Tag(models.Model):
    "Tag model"
    title = models.CharField(
        'tag title', max_length=2**6, unique=True)

    def __unicode__(self):
        return '#{0}'.format(self.title)

    def get_absolute_url(self):
        "returns absolute path for tag"
        return reverse('view_tag',
            kwargs={'tag_id': self.id})


class Post(models.Model):
    "Post model"
    pattern = re.compile(r'#(?P<title>\w+)')

    content = models.CharField(
        'message text', max_length=2**7)
    pub_date = models.DateTimeField(
        'published date', auto_now=True)
    tags = models.ManyToManyField('Tag', blank=True)
    author = models.ForeignKey(User)

    def __unicode__(self):
        return '"{0}" at {1}'.format(
            self.content, self.pub_date)

    def get_absolute_url(self):
        "returns absolute path for post"
        return reverse('post-detail',
            kwargs={'pk': self.id})

    # https://docs.djangoproject.com/en/1.6/ref/models/instances/#django.db.models.Model.save
    def save(self, *args, **kwargs):
        "saves the post"
        super(Post, self).save(*args, **kwargs)

        tags = Post.pattern.findall(self.content)
        # select * from tag where title in ('tag1', 'tag2');
        tags_existing = list(Tag.objects.filter(title__in=tags))
        tags_existing_titles = [tag.title for tag in tags_existing]

        # append missing tags as newly created ones
        for tag in tags:
            if tag not in tags_existing_titles:
                tag_new = Tag.objects.create(title=tag)
                tags_existing.append(tag_new)

        # add tags directly as a list
        self.tags = tags_existing

        logger.info("New post #{} created".format(self.pk))


