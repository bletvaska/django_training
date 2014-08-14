from django.conf.urls import patterns,  url
from pyper import views

urlpatterns = patterns('pyper.views',
    url(r'posts$',
        'all_posts', name='all_posts'),
    url(r'posts/(?P<post_id>\d+)$',
        'view_post', name='view_post'),
    url(r'tags/(?P<tag_title>\w+)$',
        'view_tag', name='view_tag'),
    url(r'tags$',
        'all_tags', name='all_tags'),
    url(r'authors$',
        'all_authors', name='all_authors'),
    url(r'authors/(?P<username>\w+)$',
        'view_author', name='view_author'),
)
