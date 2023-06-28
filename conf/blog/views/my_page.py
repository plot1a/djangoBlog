from django.shortcuts import render
from django.views import View

class Endpoint(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'my_page/page.html')