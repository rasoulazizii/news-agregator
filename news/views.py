from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import Category, Article
from .serializers import CategorySerializer, ArticleSerializer
from rest_framework.permissions import IsAuthenticated

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


class PersonalizedFeedView(generics.ListAPIView):
    serializer_class = ArticleSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user_profile = self.request.user.profile

        interested_categories = user_profile.interested_categories.all()
        if not interested_categories.exists():
            return Article.objects.none()

        queryset = Article.objects.filter(
            source__category__in=interested_categories
        ).order_by('-published_date')

        return queryset