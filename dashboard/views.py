from datetime import date, datetime, timedelta

from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render, redirect

from analytics.models import ObjectViewed
from blog.models import Category, Comment, Post
from django.db.models import Count


@login_required
def dashboard_view(request):
    title = 'Home'
    post_count = Post.objects.all().count()
    comment_number = Comment.objects.all().count()
    category_number = Category.objects.all().count()

    context = {
        'title': title,
        'post_count': post_count,
        'comment_number': comment_number,
        'category_number': category_number,
    }

    return render(request, 'dashboard/home.html', context)


@login_required
def stats_view(request):
    title = 'Stats'
    total_hit = ObjectViewed.objects.all().count()
    today_hit = ObjectViewed.objects.filter(timestamp__gt=date.today()).count()
    week_hit = ObjectViewed.objects.filter(
        timestamp__gt=date.today() - timedelta(days=7)).count()
    monthly_hit = ObjectViewed.objects.filter(
        timestamp__month=datetime.now().month).count()

    # add list of last 30 days with their ObjectViewed count as dictonery
    thirty_days_hit = []
    thirty_days_hit.append(
        {date.today().isoformat(): ObjectViewed.objects.filter(
            timestamp__gt=date.today()).count()}
    )

    for i in range(1, 30):
        thirty_days_hit.append(
            {(date.today() - timedelta(days=i)).isoformat(): ObjectViewed.objects.filter(
                timestamp__date__exact=date.today() - timedelta(days=i)).count()}
        )

    # three_month_hit

    context = {
        'title': title,
        'total_hit': total_hit,
        'today_hit': today_hit,
        'week_hit': week_hit,
        'monthly_hit': monthly_hit,
        'thirty_days_hit': thirty_days_hit,
    }

    return render(request, 'dashboard/stats.html', context)


@login_required
def category_list_view(request):
    title = 'Categories'
    category_number = Category.objects.all().count()
    category_list = Category.objects.all()

    context = {
        'title': title,
        'category_number': category_number,
        'category_list': category_list,

    }

    return render(request, 'dashboard/category_list.html', context)


@login_required
def post_list_view(request):
    title = 'Post List'
    post_number = Post.objects.all().count()

    post_list = Post.objects.all().order_by('-date_posted').annotate(
        comment_number=Count('comment'))

    page = request.GET.get('page', 1)
    paginator = Paginator(post_list, 5)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'title': title,
        'post_number': post_number,
        'posts': posts,

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
        'title': title,
        'comment_number': comment_number,
        'comments': comments,
    }

    return render(request, 'dashboard/comment_list.html', context)


@login_required
def comment_delete_view(request, pk):
    Comment.objects.get(id=pk).delete()

    return redirect('dashboard:comments')


@login_required
def post_detail_view(request, pk):
    title = 'Post Update'
    post = Post.objects.get(id=pk)
    comments = Comment.objects.filter(post__id=pk)

    context = {
        'title': title,
        'post': post,
        'comments': comments,
    }

    return render(request, 'dashboard/post_detail.html', context)
