from rest_framework import serializers
from .models import User, ToDo, Post, Comment, Album, Photo

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '_all_'

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = '_all_'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '_all_'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '_all_'

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '_all_'

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '_all_'
