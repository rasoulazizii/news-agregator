from django.db import models
from django.contrib.auth.models import User, AbstractUser
from news.models import Category

class CustomUser(AbstractUser):
    pass

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    interested_categories = models.ManyToManyField(
        Category
    )

    def __str__(self):
        return self.user.username
