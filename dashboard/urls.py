from django.urls import path

from .views import (category_list_view, comment_delete_view, comment_list_view,
                    dashboard_view, post_detail_view, post_list_view,
                    stats_view)

app_name = 'dashboard'

urlpatterns = [
    path('', dashboard_view, name='dashboard'),
    path('categories/', category_list_view, name='categories'),
    path('comments/', comment_list_view, name='comments'),
    path('comments/<int:pk>/delete', comment_delete_view, name='comment-delete'),
    path('stats/', stats_view, name='stats'),
    path('posts/', post_list_view, name='posts'),
    path('post/<int:pk>/detail/', post_detail_view, name='post-detail'),
]
