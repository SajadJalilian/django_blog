from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
from imagekit.models import ImageSpecField
from pilkit.processors import Thumbnail


class Category(models.Model):
    title = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:category-post', kwargs={'category': self.title})


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(
        upload_to='image', default='default_post_image.jpg')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)

    image_medium = ImageSpecField(source='image',
                                  processors=[Thumbnail(200, 100)],
                                  format='JPEG',
                                  options={'quality': 60})

    image_small = ImageSpecField(source='image',
                                 processors=[Thumbnail(100, 50)],
                                 format='JPEG',
                                 options={'quality': 60})

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post-detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    name = models.CharField(max_length=200)
    content = models.TextField()
    email = models.EmailField()
    pub_date = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {}'.format(self.name, self.content[:20])
