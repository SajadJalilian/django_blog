from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from .signals import object_viewed_signal
from .utilities import get_client_ip

User = settings.AUTH_USER_MODEL


class ObjectViewed(models.Model):
    user = models.CharField(max_length=1)
    ip_address = models.CharField(max_length=220, blank=True, null=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} viewed {}'.format(self.content_object, self.timestamp)

    class Meta:
        ordering = ['-timestamp']
        verbose_name = 'Object viewed'
        verbose_name_plural = 'Objects viewed'


def get_object_viewed_receiver(sender, instance, request, *args, **kwargs):
    c_type = ContentType.objects.get_for_model(sender)
    
    # IF User is authenticated, save 'U' to datebase
    # If User is anonymous, save 'A' to database
    if request.user.id is None:
        user = 'A'
    else:
        user = 'U'

    new_view_obj = ObjectViewed.objects.create(
        user=user,
        content_type=c_type,
        object_id=instance.id,
        ip_address=get_client_ip(request)
    )


object_viewed_signal.connect(get_object_viewed_receiver)
