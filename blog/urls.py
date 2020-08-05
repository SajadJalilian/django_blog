from django.urls import path

from .views import (CategoryCreateView, CategoryDeleteView,  # Post; Category
                    CategoryListView, CategoryUpdateView, PostCreateView,
                    PostDeleteView, PostListView, PostUpdateView,
                    UserPostListView, category_post_list_view,
                    post_detail_view, about)

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', post_detail_view, name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    # Category
    path('category/', CategoryListView.as_view(), name='category-list'),
    path('category/c/<str:category>/', category_post_list_view, name='category-post'),
    path('category/new/', CategoryCreateView.as_view(), name='categoy-create'),
    path('category/update/', CategoryUpdateView.as_view(), name='category-update'),
    path('category/delete/', CategoryDeleteView.as_view(), name='category-delete'),
    # About
    path('about/', about, name='blog-about'),
]
