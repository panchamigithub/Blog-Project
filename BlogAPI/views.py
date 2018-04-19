from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .models import Blog_Post, User
from .serializers import Blog_PostSerializer, UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class Blog_PostViewSet(viewsets.ModelViewSet):
    queryset = Blog_Post.objects.all()
    serializer_class = Blog_PostSerializer