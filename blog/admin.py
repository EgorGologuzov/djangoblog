from django.contrib import admin
from .models import Article, Comment, Image


admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Image)

