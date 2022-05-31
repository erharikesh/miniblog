from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Post 
# Register your models here.
@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display =['id','title', 'desc']