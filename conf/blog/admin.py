from django.contrib import admin

from blog.models import Article, User

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username',]


