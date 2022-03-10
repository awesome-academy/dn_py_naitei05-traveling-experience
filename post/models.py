from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User
from . import constants

# Create your models here.

class Profile(User):
    birthday = models.DateField(null=True, blank=True, help_text=_('Enter date of birth'))
    address = models.TextField(max_length=1000, help_text=_("Enter user's address"))
    phone = models.CharField(max_length=10, help_text=_("Enter user's phone"))
    role = models.IntegerField(choices=constants.ROLE_CHOICES, default=1)
    is_blocked = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name

class Post(models.Model):
    user = models.ForeignKey('Profile', on_delete=models.PROTECT)
    title = models.CharField(max_length=200, help_text=_('Title for this post'))
    content = models.TextField(help_text=_('Enter content of the book'))
    image = models.ImageField(upload_to ='uploads/')
    rate_average = models.DecimalField(decimal_places=2, max_digits=3, help_text=_('Rate of this post'))
    status = models.IntegerField(choices=constants.STATUS_CHOICES, default=1 , help_text=_('Status of this post (Private or Public)'))

    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey('Profile', on_delete=models.PROTECT)
    post = models.ForeignKey('Post', on_delete=models.PROTECT)
    content = models.TextField(max_length=1000)

    def __str__(self):
        return self.content

class Rate(models.Model):
    user = models.ForeignKey('Profile', on_delete=models.PROTECT)
    post = models.ForeignKey('Post', on_delete=models.PROTECT)
    point = models.DecimalField(decimal_places=2, max_digits=3, help_text=_('Point of this post'))

    def __str__(self):
        return self.point

class Follow(models.Model):
    follower_id = models.ForeignKey('Profile', on_delete=models.PROTECT, related_name='follower')
    followed_id = models.ForeignKey('Profile', on_delete=models.PROTECT, related_name='followed')

class Tag(models.Model):
    content = models.CharField(max_length=200, help_text=_('Enter content for this tag'))

    def __str__(self):
        return self.content

class PostTag(models.Model):
    tag = models.ForeignKey('Tag', on_delete=models.PROTECT)
    post = models.ForeignKey('Post', on_delete=models.PROTECT)
