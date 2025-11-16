from django.db import models
from django.contrib.auth.models import User
from news.models import Category

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    interested_categories = models.ManyToManyField(
        Category
    )
