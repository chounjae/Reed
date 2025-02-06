from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.


class PostDash(models.Model) :
    title = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, default=0)
    date = models.DateField(auto_now=True)
    main = models.TextField()
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_dash')
    dislike_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='dislike_dash')
    def __str__(self) :
        return self.title
class Comment(models.Model) :
    dash = models.ForeignKey('PostDash', on_delete = models.CASCADE, default=0)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, default=1)
    mains = models.TextField()
    date = models.DateField(auto_now=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_da')
    dislike_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='dislike_da')

    def __str__(self) :
        return self.mains
class User(AbstractUser) :
    pass
    def __str__(self) :
        return self.username