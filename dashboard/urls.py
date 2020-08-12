from django.urls import include, path

from .views import (category_list_view, comment_list_view, dashboard_view,
                    post_detail_view, post_list_view, stats_view)

app_name = 'dashboard'

urlpatterns = [
    path('', dashboard_view , name='dashboard'),
    path('categories/', category_list_view , name='categories'),
    path('comments/', comment_list_view , name='comments'),
    path('stats/', stats_view , name='stats'),
    path('posts/', post_list_view , name='posts'),
    path('post/detail/', post_detail_view , name='post-update'),
]
