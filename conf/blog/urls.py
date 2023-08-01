from django.urls import path
from blog.views.main import (RenderMainPageView, ArticleDetailView, AuthRenderView,
                             RegistrRenderView, UserLogoutView, LikeCreateViews, CommentCreateDeleteView,
                             UserCabinetRenderView, ArticleRenderCreateView, ArticleDeleteView,
                             RenderArticlesListView)

urlpatterns = [
    path('', RenderMainPageView.as_view(), name='home'),
    path('articles/list/', RenderArticlesListView.as_view(), name='list_articles'),
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name='detail'),
    path('auth/', AuthRenderView.as_view(), name='auth'),
    path('registr/', RegistrRenderView.as_view(), name='registr'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('likes/', LikeCreateViews.as_view(), name='like'),
    path('articles/<int:article_pk>/comments/', CommentCreateDeleteView.as_view(), name='comments'),
    path('comments/<int:comment_pk>/', CommentCreateDeleteView.as_view(), name='comment_delete'),
    path('users/', UserCabinetRenderView.as_view(), name='user'),
    path('articles/', ArticleRenderCreateView.as_view(), name='article'),
    path('articles/<int:article__pk>/', ArticleDeleteView.as_view(), name='article_delete'),

]
