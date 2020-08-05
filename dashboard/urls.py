from django.urls import include, path

from .views import (category_list, comment_list, post_list,
                    post_detail, dashboard_view, stats)

app_name = 'dashboard'

urlpatterns = [
    path('', dashboard_view , name='home'),
    path('categories', category_list , name='categories'),
    path('comments', comment_list , name='comments'),
    path('stats', stats , name='stats'),
    path('posts', post_list , name='posts'),
    path('post/update', post_detail , name='post-update'),
]
