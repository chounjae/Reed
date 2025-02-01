from django.contrib import admin
from .models import PostDash, Comment, User
# Register your models here.


admin.site.register(PostDash)
admin.site.register(Comment)
admin.site.register(User)