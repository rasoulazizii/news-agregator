from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import Category, Article
from .serializers import CategorySerializer, ArticleSerializer

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (AllowAny,) 

class ArticleListView(generics.ListAPIView):
    queryset = Article.objects.all().order_by('-published_date')
    serializer_class = ArticleSerializer
    permission_classes = (AllowAny,)

class ArticleDetailView(generics.RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (AllowAny,)