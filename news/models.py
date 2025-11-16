from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=220)
    slug = models.SlugField()

class NewSource(models.Model):
    name = models.CharField(max_length=220)
    website_url = models.URLField()
    rss_feed_url = models.URLField()
    is_active = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Article(models.Model):
    source = models.ForeignKey(NewSource, on_delete=models.CASCADE)
    title = models.CharField(max_length=220)
    link = models.URLField()
    description = models.TextField()
    published_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

