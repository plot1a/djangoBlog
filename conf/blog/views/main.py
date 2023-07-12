from django.contrib.auth import authenticate, logout
from django.shortcuts import render, redirect
from django.views import View
from blog.models import Article, User


class RenderMainPageView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()
        return render(request, "blog/main_page.html", context={
            'articles': articles
        })


class ArticleDetailView(View):
    def get(self, request, *args, **kwargs):
        article = Article.objects.get(id=kwargs['pk'])
        return render(request, 'blog/detail_page.html', context={'item': article})


class AuthRenderView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'blog/autorization.html', )

    def post(self, request, *args, **kwargs):
        user = User.objects.filter(username=request.POST['username'])
        if user.exists():
            if user.first().check_password(request.POST['password']):
                authenticate(username=request.POST['username'],
                             password=request.POST['password'])
                return redirect('home')
        return render(request, 'blog/autorization.html', context={'error': 'Неверный логин или пароль'})


class RegistrRenderView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'blog/registr.html', )

    def post(self, request, *args, **kwargs):
        user = User.objects.filter(username=request.POST['username'])
        try:
            User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password'],
                email=request.POST['email']
            )
            return redirect('auth')
        except Exception as error:
            return render(request, 'blog/registr.html', context={'error': error})


class UserLogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('home')
