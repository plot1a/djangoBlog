from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название статьи')
    image = models.ImageField(upload_to='article/', verbose_name='Фото')
    content = models.TextField(verbose_name='Содержание статьи')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обнавления')
    author = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name='Автор')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'


class User(AbstractUser):
    """Overriding the User model with the email field as primary"""

    username = models.CharField(
        max_length=150,

        verbose_name="Username",
        unique=True,
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    photo = models.ImageField(upload_to='user/', verbose_name='Фото')

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'users'
        app_label = 'blog'
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Like(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name='Пользователи')
    article = models.ForeignKey('Article', on_delete=models.CASCADE, verbose_name='Статья')

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = 'likes'
        app_label = 'blog'
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'
        unique_together = ['user', 'article']


class Comment(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name='Коментаторы')
    content = models.CharField(max_length=150, verbose_name='Коментарий')
    article = models.ForeignKey('Article', on_delete=models.CASCADE, verbose_name='Статья')

    def __str__(self):
        return f'{self.user.username}, {self.content}'

    class Meta:
        db_table = 'comment'
        app_label = 'blog'
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
