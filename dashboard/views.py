from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from blog.models import Category, Comment, Post


def dashboard_view(request):
    title = 'Home'

    context = {
        'title' : title,
    }
    
    return render(request, 'dashboard/home.html', context)

def stats(request):
    title = 'Stats'

    context = {
        'title' : title,
    }
    
    return render(request, 'dashboard/stats.html', context)


def category_list(request):
    title = 'Categories'

    context = {
        'title' : title,
    }
    
    return render(request, 'dashboard/category_list.html', context)


def post_list(request):
    title = 'Post List'

    context = {
        'title' : title,
    }
    
    return render(request, 'dashboard/post_list.html', context)


def comment_list(request):
    title = 'Comment List'

    context = {
        'title' : title,
    }
    
    return render(request, 'dashboard/comment_list.html', context)


def post_detail(request):
    title = 'Post Update'

    context = {
        'title' : title,
    }
    
    return render(request, 'dashboard/post_detail.html', context)
