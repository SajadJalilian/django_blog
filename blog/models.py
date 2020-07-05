from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse

class Category(models.Model):
    title = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
        

class Comment(models.Model):
    name = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)
    article = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {}'.format(self.name, self.content[:20])