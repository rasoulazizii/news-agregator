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


