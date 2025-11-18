from django.contrib import admin
from .models import Category, NewsSource, Article

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)} 

@admin.register(NewsSource)
class NewsSourceAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'website_url', 'is_active')
    list_filter = ('is_active', 'category')
    search_fields = ('name', 'website_url')

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'source', 'published_date')
    list_filter = ('source', 'published_date')
    search_fields = ('title', 'description')
    def has_add_permission(self, request):
        return False