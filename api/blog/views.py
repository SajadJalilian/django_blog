from rest_framework import viewsets

from blog.models import Post

from .serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-date_posted')
    serializer_class = PostSerializer


# TODO add ViewSet for Category and Comment