from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, render
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from analytics.signals import object_viewed_signal

from .forms import CommentForm
from .models import Category, Comment, Post


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


def post_detail_view(request, pk):

    post = get_object_or_404(Post, id=pk)
    comments = Comment.objects.filter(post=post).order_by('-id')

    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            content = request.POST.get('content')
            name = request.POST.get('name')
            email = request.POST.get('email')

            comment = Comment.objects.create(post=post, content=content, name=name, email=email)
            comment.save()
    else:
        comment_form = CommentForm

    context = {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
    }

    object_viewed_signal.send(post.__class__, instance=post, request=request)

    return render(request, 'blog/post_detail.html', context)


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/post_create.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/post_create.html'

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
    template_name = 'blog/post_confirm_delete.html'

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


def category_post_list_view(request, category):
    cats = Post.objects.filter(categories__title=category).order_by('-date_posted')

    page = request.GET.get('page', 10)

    paginator = Paginator(cats, 10)
    try:
        cat = paginator.page(page)
    except PageNotAnInteger:
        cat = paginator.page(1)
    except EmptyPage:
        cat = paginator.page(paginator.num_pages)

    return render(request, 'blog/category_post.html', {'category_post':cat, 'category':category})


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    fields = ['title']


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    fields = ['title']


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    success_url = '/'


# class CommentCreateView(CreateView):
#     model = Comment
#     template_name = 'blog/post_detail.html'

#     fields = ['name', 'content','email']

#     def form_valid(self, form):
#         return super().form_valid(form)

# class CommentDeleteView(DeleteView):
#     model = Comment


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
