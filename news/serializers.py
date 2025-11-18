from rest_framework import serializers
from .models import Category, Article, NewsSource

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'slug')

class ArticleSerializer(serializers.ModelSerializer):
    source = serializers.CharField(source='source.name', read_only=True)

    class Meta:
        model = Article
        fields = ('id', 'title', 'link', 'description', 'published_date', 'source')


