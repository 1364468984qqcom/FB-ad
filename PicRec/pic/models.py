import datetime
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

# today = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


class Pic(models.Model):
    created = models.DateTimeField(auto_now=True)
    pid = models.IntegerField(primary_key=True)
    url = models.CharField(max_length=5000, default='')
    images = models.TextField(max_length=50000, default='')

    class Meta:
        ordering = ('created',)


class Pic1(models.Model):
    created = models.DateTimeField(auto_now=True)
    pid = models.IntegerField(primary_key=True, default=1)
    similar_rate = models.TextField(max_length=1000000000, default='')

    class Meta:
        ordering = ('pid',)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
