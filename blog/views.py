from django.shortcuts import render

posts = [
    {
        'author': 'Sajad',
        'title': 'Blog Post 1',
        'content': 'First blog post',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Rana',
        'title': 'Blog Post 2',
        'content': 'First blog post',
        'date_posted': 'August 28, 2018'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
