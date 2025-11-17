from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=220)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class NewsSource(models.Model):
    name = models.CharField(max_length=220)
    website_url = models.URLField()
    rss_feed_url = models.URLField(unique=True)
    is_active = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Article(models.Model):
    source = models.ForeignKey(NewsSource, on_delete=models.CASCADE)
    title = models.CharField(max_length=220)
    link = models.URLField(unique=True)
    description = models.TextField()
    published_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

