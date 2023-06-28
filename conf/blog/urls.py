from django.urls import path
from blog.views.main import RenderMainPageView
from blog.views.my_page import Endpoint

urlpatterns = [
    path('', RenderMainPageView.as_view()),
    path('page/', Endpoint.as_view())
]