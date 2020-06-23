from django.urls import path
from .views import (
    # Post
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    CategoryPostListView,
    # Category
    CategoryListView,
    CategoryCreateView,
    CategoryUpdateView,
    CategoryDeteleView,
    # Comment
    CommentListView,
    CommentCreateView,
    CommentDeleteView
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    # Category
    path('category/', CategoryListView.as_view(), name='category-list'),
    path('category/<str:title>', CategoryPostListView.as_view(), name='category-post-list'),
    path('category/new/', CategoryCreateView.as_view(), name='categoy-create'),
    path('category/update/', CategoryUpdateView.as_view(), name='category-update'),
    path('category/delete/', CategoryDeteleView.as_view(), name='category-delete'),
    # Comment
    path('comment/create/', CommentCreateView.as_view(), name='comment-create'),
    path('comment/delete/', CommentDeleteView.as_view(), name='comment-delete'),
    # About
    path('about/', views.about, name='blog-about'),
]
