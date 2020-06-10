from django.urls import path, include
from rest_framework import routers
from api.blog.views import PostViewSet
from api.users.views import ProfileViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'post', PostViewSet)
router.register(r'profile', ProfileViewSet)
router.register(r'user', UserViewSet)


urlpatterns = [
    path('v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
