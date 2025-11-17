from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Profile

admin.site.register(CustomUser, UserAdmin)

@admin.register(Profile)
class ProflieAdmin(admin.ModelAdmin):
    list_display = ('user',)
    filter_horizontal = ('interested_categories',)
    
