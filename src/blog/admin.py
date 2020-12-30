from django.contrib import admin
from .models import Category, Post, PostView, Comment, Like

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(PostView)
admin.site.register(Comment)
admin.site.register(Like)
