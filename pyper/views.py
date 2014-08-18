from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
)
from pyper.models import Post, Tag

class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

    # def get_context_data(self, **kwargs):
    #     context = super(PostDetailView, self).get_context_data(**kwargs)
    #     context['tags'] = self.object.tags.all()
    #     # context['object'].tags.all()
    #     return context


class PostCreateView(CreateView):
    model = Post
    template_name = 'post_create.html'
    fields = ['content', 'author']

    def get_success_url(self):
        return reverse('post_list')


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
