from rest_framework import serializers
from social.models import User, Comment, Tag, Follower, Post, PostLikes

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('__all__')

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('__all__')

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('__all__')

class FollowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follower
        fields = ('__all__')

class PostLikesSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())

    class Meta:
        model = PostLikes
        fields = ('__all__')

    