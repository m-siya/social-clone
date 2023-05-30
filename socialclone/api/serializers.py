from rest_framework import serializers
from social.models import (User, Comment, Tag, Follower, Post, PostLikes, 
                    CommentLikes, UserFollowsTag, Repost, PostTag, CommentTag)

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
    #post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())

    class Meta:
        model = PostLikes
        fields = ('__all__')

class CommentLikesSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    comment = serializers.PrimaryKeyRelatedField(queryset=Comment.objects.all())

    class Meta:
        model = CommentLikes
        fields = ('__all__')

class tagfollowserializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset = User.objects.all())
    #tag = serializers.PrimaryKeyRelatedField(queryset = Tag.objects.all())

    class Meta:
        model = UserFollowsTag
        fields = ('__all__')

class RepostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Repost
        fields = ('__all__')

class PostTagSerializer(serializers.ModelSerializer):
    post = serializers.PrimaryKeyRelatedField(queryset = Post.objects.all())
    class Meta:
        model = PostTag
        fields = ('__all__')

class CommentTagSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CommentTag
        fields = ('__all__')