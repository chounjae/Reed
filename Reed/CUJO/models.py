from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class PostDash(models.Model) :
    title = models.CharField(max_length=50)
    author = models.ForeignKey('Author', on_delete = models.CASCADE)
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
    author = models.ForeignKey('Author', on_delete = models.CASCADE)
    date = models.DateField(auto_now=True)
    main = models.TextField()
    like = models.IntegerField(default=0)
    unlike = models.IntegerField(default=0)

class User(AbstractUser) :
    pass