from rest_framework import serializers
from .models import Blog_Post, User

class Blog_PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog_Post
        fields = ('blogpost','author','username',)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'mobile', 'password', 'city' , 'ans',)
