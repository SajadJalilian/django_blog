from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post, Category, Comment


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


# def PostDetailView(request, title):
#     post = Post.objects.get(title=title)
#     user = request.username()
#     return render(request, 'blog/post_detail.html', {'object':post, 'user':user})

class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class CategoryListView(ListView):
    model = Category
    template_object_name = 'blog/category_list.html'
    context_object_name = 'categories'
    ordering = ['title']


def CategoryPostListView(request, category):
    cats = Post.objects.filter(categories__title=category)

    # page = request.GET.get('page', 1)

    # paginator = Paginator(cats, 10)
    # try:
    #     cat = paginator.page(page)
    # except PageNotAnInteger:
    #     cat = paginator.page(1)
    # except EmptyPage:
    #     cat = paginator.page(paginator.num_pages)

    return render(request, 'blog/category_post.html', {'post':cats})



class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    fields = ['title']


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    fields = ['title']


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    success_url = '/'


class CommentListView(ListView):
    model = Comment
    context_object_name = 'comments'
    ordering = ['-pub_date']


class CommentCreateView(CreateView):
    model = Comment
    fields = ['name', 'content']


class CommentDeleteView(DeleteView):
    model = Comment


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
