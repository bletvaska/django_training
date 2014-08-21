import logging
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from pyper.models import Post, Tag

logger = logging.getLogger(__name__)

class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'

    class Meta:
        ordering = ['-pub_date']


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class PostCreateView(CreateView):
    model = Post
    template_name = 'post_form.html'
    fields = ['content', 'author']

    def get_context_data(self, **kwargs):
            context = super(PostCreateView, self).get_context_data(**kwargs)
            context['target'] = reverse('post-create')
            return context

    def get_success_url(self):
        return reverse('post-list')


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'post_form.html'
    fields = ['content', 'author']

    def get_context_data(self, **kwargs):
            context = super(PostUpdateView, self).get_context_data(**kwargs)
            context['target'] = reverse('post-edit', kwargs = {'pk': self.get_object().pk})
            return context


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'

    def get_success_url(self):
        return reverse('post-list')


class TagDetailView(DetailView):
    model = Tag
    template_name = 'tag_detail.html'
    slug_field = 'title'
    slug_url_kwarg = 'title'


class TagListView(ListView):
    model = Tag
    template_name = 'tag_list.html'


class AuthorListView(ListView):
    model = User
    template_name = 'author_list.html'

class AuthorDetailView(DetailView):
    model = User
    template_name = 'author_detail.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'


# ____  _____ ____ _____      _    ____ ___
#|  _ \| ____/ ___|_   _|    / \  |  _ \_ _|
#| |_) |  _| \___ \ | |     / _ \ | |_) | |
#|  _ <| |___ ___) || |    / ___ \|  __/| |
#|_| \_\_____|____/ |_|   /_/   \_\_|  |___|
#


from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework import viewsets

class PostReadUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    model = Post

class PostCreateReadView(ListCreateAPIView):
    model = Post


from pyper.serializers import TagSerializer, PostSerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
