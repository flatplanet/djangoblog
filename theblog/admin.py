from django.contrib import admin
from .models import Post, Category, Profile, Comment

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(Comment)
