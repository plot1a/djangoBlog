from django.shortcuts import render
from django.views import View



class RenderMainPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'blog/main_page.html')