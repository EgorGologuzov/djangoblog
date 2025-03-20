from django.contrib import admin
from .models import Article, Comment, Image, Category


admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Image)
admin.site.register(Category)

