from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.ArticleList.as_view(), name='article_list'),
    path('post/<int:pk>', views.ArticleDetail.as_view(), name='article_detail'),
    path('post/new/', views.CreateArticleView.as_view(), name='article_new'),
    path('post/<int:pk>/edit/', views.ArticleUpdateView.as_view(), name='article_edit'),
    path('post/<int:pk>/remove/', views.ArticleDeleteView.as_view(), name='article_remove'),
    path('post/<int:pk>/publish/', views.article_publish, name='article_publish')


]
