from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


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
    category_number = Category.objects.all().count()
    category_list = Category.objects.all()

    context = {
        'title' : title,
        'category_number' : category_number,
        'category_list': category_list,

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
    comment_number = Comment.objects.all().count()
    comment_list = Comment.objects.all().order_by('-pub_date')

    page = request.GET.get('page', 1)

    paginator = Paginator(comment_list, 5)

    try:
        comments = paginator.page(page)
    except PageNotAnInteger:
        comments = paginator.page(1)
    except EmptyPage:
        comments = paginator.page(paginator.num_pages)


    context = {
        'title' : title,
        'comment_number' : comment_number,
        'comments' : comments,
    }
    
    return render(request, 'dashboard/comment_list.html', context)


@login_required
def post_detail_view(request):
    title = 'Post Update'

    context = {
        'title' : title,
    }
    
    return render(request, 'dashboard/post_detail.html', context)
