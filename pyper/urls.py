from django.conf.urls import patterns,  url
from pyper import views

urlpatterns = patterns('',

    url(r'posts$',
        views.PostListView.as_view( ),
        name="post_list"),

    url(r'posts/(?P<pk>\d+)$',
        views.PostDetailView.as_view(),
        name="post_detail"),

    url(r'posts/new$',
        views.PostCreateView.as_view(),
        name="post_create"),

    url(r'tags$',
        views.TagListView.as_view(),
        name='tag_list'),

    url(r'tags/(?P<title>\w+)$',
        views.TagDetailView.as_view(),
        name='tag_detail'),

    url(r'authors$',
        views.AuthorListView.as_view(),
        name='author_list'),

    url(r'authors/(?P<username>\w+)$',
        views.AuthorDetailView.as_view(),
        name='author_detail'),
)
