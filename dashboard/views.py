from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from blog.models import Category, Comment, Post


@login_required
def dashboard_view(request):
    title = 'Home'
    post_count = Post.objects.all().count()
    comment_number = Comment.objects.all().count()
    category_number = Category.objects.all().count()


    context = {
        'title' : title,
        'post_count' : post_count,
        'comment_number' : comment_number,
        'category_number' : category_number,
    }
    
    return render(request, 'dashboard/home.html', context)


@login_required
def stats_view(request):
    title = 'Stats'

    context = {
        'title' : title,
    }
    
    return render(request, 'dashboard/stats.html', context)


@login_required
def category_list_view(request):
    title = 'Categories'

    context = {
        'title' : title,
    }
    
    return render(request, 'dashboard/category_list.html', context)


@login_required
def post_list_view(request):
    title = 'Post List'

    context = {
        'title' : title,
    }
    
    return render(request, 'dashboard/post_list.html', context)


@login_required
def comment_list_view(request):
    title = 'Comment List'

    context = {
        'title' : title,
    }
    
    return render(request, 'dashboard/comment_list.html', context)


@login_required
def post_detail_view(request):
    title = 'Post Update'

    context = {
        'title' : title,
    }
    
    return render(request, 'dashboard/post_detail.html', context)
