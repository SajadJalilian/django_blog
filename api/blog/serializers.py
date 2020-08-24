from rest_framework import serializers

from blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'content', 'date_posted', 'author']

# TODO: add Serializers for Category and Comment
