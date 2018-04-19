from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Blog_Post,User

admin.site.register(Blog_Post)
admin.site.register(User)