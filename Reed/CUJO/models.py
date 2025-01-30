from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.


class PostDash(models.Model) :
    title = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, default=0)
    date = models.DateField(auto_now=True)
    main = models.TextField()
    like = models.IntegerField(default=0)
    unlike = models.IntegerField(default=0)

    def __str__(self) :
        return self.title
class Author(models.Model) :
    name = models.CharField(max_length=10)
    email = models.EmailField()

    def __str__(self) :
        return self.name
class Comment(models.Model) :
    dash = models.ForeignKey('PostDash', on_delete = models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, default=0)
    date = models.DateField(auto_now=True)
    main = models.TextField()
    like = models.IntegerField(default=0)
    unlike = models.IntegerField(default=0)
class User(AbstractUser) :
    pass
    def __str__(self) :
        return self.username