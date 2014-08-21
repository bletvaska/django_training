from rest_framework import serializers
from pyper.models import Tag, Post

class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag


class PostSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.HyperlinkedRelatedField(
        view_name = 'author_detail', # user-detail
        lookup_field = 'username',
    )
    class Meta:
        model = Post
