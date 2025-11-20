from django.urls import path
from .views import CategoryListView, ArticleListView, ArticleDetailView, PersonalizedFeedView

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('articles/', ArticleListView.as_view(), name='article-list'),
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('feed/', PersonalizedFeedView.as_view(), name='personalized-feed'),
]