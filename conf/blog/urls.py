from django.urls import path
from blog.views.main import (RenderMainPageView, ArticleDetailView, AuthRenderView,
                                                 RegistrRenderView, UserLogoutView, LikeCreateViews, CommentCreateDeleteView)

urlpatterns = [
    path('', RenderMainPageView.as_view(), name='home'),
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name='detail'),
    path('auth/', AuthRenderView.as_view(), name='auth'),
    path('registr/', RegistrRenderView.as_view(), name='registr'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('likes/', LikeCreateViews.as_view(), name='like'),
    path('articles/<int:article_pk>/comments/', CommentCreateDeleteView.as_view(), name='comments'),
    path('comments/<int:comment_pk>/', CommentCreateDeleteView.as_view(), name='comment_delete')

]
