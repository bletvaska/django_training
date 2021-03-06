from django.conf.urls import patterns,  url
from rest_framework.routers import DefaultRouter
from pyper import views


urlpatterns = patterns('',

    url(r'^posts$',
        views.PostListView.as_view( ),
        name="post-list"),

    url(r'^posts/(?P<pk>\d+)$',
        views.PostDetailView.as_view(),
        name="post-detail"),

    url(r'^posts/new$',
        views.PostCreateView.as_view(),
        name="post-create"),

    url(r'^posts/(?P<pk>\d+)/edit$',
        views.PostUpdateView.as_view(),
        name="post-edit"),

    url(r'^posts/(?P<pk>\d+)/delete$',
        views.PostDeleteView.as_view(),
        name="post-delete"),

    url(r'^tags$',
        views.TagListView.as_view(),
        name='tag-list'),

    url(r'^tags/(?P<title>\w+)$',
        views.TagDetailView.as_view(),
        name='tag-detail'),

    url(r'^authors$',
        views.AuthorListView.as_view(),
        name='author-list'),

    url(r'^authors/(?P<username>\w+)$',
        views.AuthorDetailView.as_view(),
        name='author-detail'),

# ____  _____ ____ _____      _    ____ ___
#|  _ \| ____/ ___|_   _|    / \  |  _ \_ _|
#| |_) |  _| \___ \ | |     / _ \ | |_) | |
#|  _ <| |___ ___) || |    / ___ \|  __/| |
#|_| \_\_____|____/ |_|   /_/   \_\_|  |___|
#

    # url(r'^api/v1/posts$',
    #     views.PostCreateReadView.as_view(),
    #     name='post_rest_api'),

    # url(r'^api/v1/posts/(?P<pk>\d+)$',
    #     views.PostReadUpdateDeleteView.as_view(),
    #     name='post_rest_api'),

    # url(r'^api/v1/tags$',
    #     views.TagViewSet.as_view(),
    #     name='tag-rest-api'),
)


# router = DefaultRouter()
# router.register(r'api/v3/tags', views.TagViewSet)
# router.register(r'api/v3/posts', views.PostViewSet)
# urlpatterns += router.urls
