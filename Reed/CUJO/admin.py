from django.contrib import admin
from .models import PostDash, Comment, Author, User
# Register your models here.


admin.site.register(PostDash)
admin.site.register(Comment)
admin.site.register(Author)
admin.site.register(User)