from django.shortcuts import render
from django.contrib.auth.models import User
from pyper.models import Post, Tag


def all_posts(request):
    "shows all posts"
    posts = Post.objects.order_by('-pub_date')
    return render(request, 'posts.html', {'posts': posts})


def view_post(request, post_id):
    "shows single post "
    post = Post.objects.get(pk=post_id)
    return render(request, 'post.html',
                  {'post': post, 'tags': post.tags.all()})


def view_tag(request, tag_title):
    "shows single tag"
    tag = Tag.objects.get(title=tag_title)
    return render(request, 'tag.html', {'tag': tag, 'posts': tag.post_set.all()})


def all_tags(request):
    "shows all tags"
    tags = Tag.objects.all()
    return render(request, 'tags.html', {'tags': tags})


def view_author(request, username):
    "shows author"
    author = User.objects.get(username=username)
    posts = author.post_set.all()
    return render(request, 'author.html', {'author': author, 'posts': posts})


def all_authors(request):
    "shows all users"
    users = User.objects.all()
    return render(request, 'authors.html', {'authors': users})
