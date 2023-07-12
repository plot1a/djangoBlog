from django.urls import path
from blog.views.main import RenderMainPageView, ArticleDetailView, AuthRenderView, RegistrRenderView, UserLogoutView

urlpatterns = [
    path('', RenderMainPageView.as_view(), name='home'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name = 'detail'),
    path('auth/', AuthRenderView.as_view(), name='auth'),
    path('registr/', RegistrRenderView.as_view(), name='registr'),
    path('logout/', UserLogoutView.as_view(), name='logout')
]
