from django.contrib import admin

from blog.models import Article, User, Like, Comment


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username',]


@admin.register(Like)
class likeAdmin(admin.ModelAdmin):
    list_display = ['user', 'article']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'content']
