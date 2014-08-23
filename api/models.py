from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    """

    """
    user = models.OneToOneField(User, verbose_name="django authentication user", related_name='user_profile')
    peers = models.ForeignKey(User, related_name='peers')

    def __unicode__(self):
        return "%s " % self.user.username


# Create your models here.
class Item(models.Model):
    """
    An Item
    """
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    provider = models.ForeignKey(User, related_name='items')
    consumer = models.ForeignKey(User, null=True, blank=True, related_name='items')


class Transaction(models.Model):
    item = models.ForeignKey(Item, related_name='items')



