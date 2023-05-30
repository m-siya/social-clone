from rest_framework.response import Response
from social.models import (User, Post, Comment, Tag, Follower, PostLikes, CommentLikes,
                            UserFollowsTag, Repost, PostTag, CommentTag)
from .serializers import (UserSerializer, PostSerializer, CommentSerializer, TagSerializer, FollowerSerializer, 
PostLikesSerializer, CommentLikesSerializer, tagfollowserializer, RepostSerializer, PostTagSerializer, 
CommentTagSerializer)

from rest_framework import generics
from django.shortcuts import get_object_or_404

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    model = User
    serializer_class = UserSerializer
    def get_object(self, queryset=None):

        return User.objects.get(user_id_text=self.kwargs.get("user_id_text"))

#post - make, delete, like, unlike, view all posts
#view all posts and make post
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

#delete post
class DeletePost(generics.RetrieveDestroyAPIView):
    model = Post
    serializer_class = PostSerializer
    def get_object(self, queryset=None):
        return Post.objects.get(post_id_text=self.kwargs.get("post_id_text"))
    
#like and unlike post
class LikePost(generics.CreateAPIView):
    serializer_class = PostLikesSerializer

    def get_queryset(self):
        user_id = self.request.data.get('user_id')
        post_id = self.request.data.get('post_id')
        return PostLikes.objects.filter(user_id=user_id, post_id=post_id)

    def post(self, request, *args, **kwargs):
        # Check if the user has already liked the post
        existing_like = self.get_queryset().first()

        if existing_like:
            # If the user has already liked the post, remove the like
            return Response({'detail': 'Post already liked.'})
        else:
            # If the user has not liked the post, create a new like
            return self.create(request, *args, **kwargs)

class UnlikePost(generics.RetrieveDestroyAPIView):
    model = PostLikes
    serializer_class = PostLikesSerializer
    def get_object(self, queryset=None):
        return PostLikes.objects.get(post_likes_id_text=self.kwargs.get("post_likes_id_text"))



# Repost Views - repost a post, delete a repost
class MakeRepost(generics.CreateAPIView):
    serializer_class = RepostSerializer

    def perform_create(self, serializer):
        #find the user whose post is being reposted
        #print(self.request.data)
        post_id_text = self.request.data.get('post')
      #  post_id_text = self.kwargs['post']
        #print(post_id_text)
        post = Post.objects.get(post_id_text = post_id_text)
       # print(post)
        user_id_text = post.user_id
        user = User.objects.get(user_id_text = user_id_text)

        if serializer.is_valid():
            serializer.save(reposted_from_user=user)

class DeleteRepost(generics.RetrieveDestroyAPIView):
    serializer_class = RepostSerializer
    model = Repost
    def get_object(self, queryset=None):
        return Repost.objects.get(repost_id_text=self.kwargs.get("repost_id_text"))
        
# follower views
# add follower, remove follower, view all follower, view all following
#view all entries
# class FollowerList(generics.ListAPIView):
#     queryset = Follower.objects.all()
#     serializer_class = FollowerSerializer

# add follower
class AddFollower(generics.CreateAPIView):
    serializer_class = FollowerSerializer

    def get_queryset(self):
        user_id = self.request.data.get('user')
        follower_id = self.request.data.get('follower')
        return Follower.objects.filter(user=user_id, is_followed_by=follower_id)

    def post(self, request, *args, **kwargs):
        # Check if the follower has already followed the user
        existing_follower = self.get_queryset().first()

        if existing_follower:
            # If the user has already followed, remove 
            return Response({'detail': 'User already followed.'})
        else:
            # If the user has not followed, create a new follower
            return self.create(request, *args, **kwargs)

# remove follower
class RemoveFollower(generics.DestroyAPIView):
    model = Follower
    serializer_class = FollowerSerializer
    def get_object(self, queryset=None):
        return Follower.objects.get(follower_id_text=self.kwargs.get("follower_id_text"))

# view all followers
class Followers(generics.ListAPIView):
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer

    def get_queryset(self):
        user_id_text = self.kwargs["user_id_text"]
        user = User.objects.get(user_id_text=user_id_text)
        return Follower.objects.filter(user = user).exclude(is_followed_by = user)

# view following
class Following(generics.ListAPIView):
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer

    def get_queryset(self):
        user_id_text = self.kwargs["user_id_text"]
        user = User.objects.get(user_id_text= user_id_text)
        return Follower.objects.filter(is_followed_by = user)


#comments - post comment, like/unlike comments, delete comments, view all comments
#view/post comment
class Comments(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

#delete comment
class commentDelete(generics.DestroyAPIView):
    model = Comment
    serializer_class = CommentSerializer
    def get_object(self, queryset = None):
        return Comment.objects.get(comment_id_text=self.kwargs.get("comment_id_text"))

# like/unlike comments
class LikeComment(generics.CreateAPIView):
    serializer_class = CommentLikesSerializer

    def get_queryset(self):
        user_id = self.request.data.get('user_id')
        comment_id = self.request.data.get('comment_id')
        return CommentLikes.objects.filter(user_id=user_id, comment_id=comment_id)

    def post(self, request, *args, **kwargs):
        # Check if the user has already liked the comment
        existing_like = self.get_queryset().first()

        if existing_like:
            # If the user has already liked the comment, remove the like
            return Response({'detail': 'Comment already liked'})
        else:
            # If the user has not liked the comment, create a new like
            return self.create(request, *args, **kwargs)

class UnlikeComment(generics.DestroyAPIView):
    model = CommentLikes
    serializer_class = CommentLikesSerializer
    def get_object(self, queryset=None):
        return CommentLikes.objects.get(comment_likes_id_text=self.kwargs.get("comment_likes_id_text"))


#tags - follow/unfollow, create/delete
#create or delete tags
class Tags(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class DeleteTag(generics.DestroyAPIView):
    model = Tag
    serializer_class = TagSerializer
    def get_object(self, queryset=None):
        return Tag.objects.get(tag_name=self.kwargs.get("tag_name"))

#follow/unfollow tags
class FollowTag(generics.CreateAPIView):
    serializer_class = tagfollowserializer

    def get_queryset(self):
        user_id = self.request.data.get('user')
        tag_name = self.request.data.get('tag')
        return UserFollowsTag.objects.filter(user=user_id, tag_name=tag_name)

    def post(self, request, *args, **kwargs):
        # Check if the user has already followed the tag
        followed_tag = self.get_queryset().first()

        if followed_tag:
            # If the user already follows tag, remove 
            return Response({'detail': 'Tag already followed.'})
        else:
            # If the user does not follow tag, create a new followed tag
            return self.create(request, *args, **kwargs)
        

class UnfollowTag(generics.DestroyAPIView):
    model = UserFollowsTag
    serializer_class = tagfollowserializer
    def get_object(self, queryset=None):
        return UserFollowsTag.objects.get(user_follows_tag_id_text=self.kwargs.get("user_follows_tag_id_text"))

# views for post tags - add tag to post, remove tag from post, view all tags for a post
# add tag to post
class AddPostTag(generics.CreateAPIView):
    serializer_class = PostTagSerializer

# remove tag from post
class RemovePostTag(generics.RetrieveDestroyAPIView):
    model = PostTag
    serializer_class = PostTagSerializer

    def get_object(self, queryset=None):
        return PostTag.objects.get(post_tag_id_text=self.kwargs.get("post_tag_id_text"))

# view all tags for a post
class ViewPostTags(generics.ListAPIView):
    serializer_class = PostTagSerializer
    queryset = PostTag.objects.all()

    def get_queryset(self):
        post_id_text = self.kwargs["post_id_text"]
        return PostTag.objects.filter(post_id=post_id_text)
    
# views for comment tags - add tag to comment, remove tag from comment, view all tags for a comment
# add tag to comment
class AddCommentTag(generics.CreateAPIView):
    serializer_class = CommentTagSerializer

# remove tag from comment
class RemoveCommentTag(generics.RetrieveDestroyAPIView):
    model = CommentTag
    serializer_class = CommentTagSerializer

    def get_object(self, queryset=None):
        return CommentTag.objects.get(comment_tag_id_text=self.kwargs.get("comment_tag_id_text"))

# view all tags for a post
class ViewCommentTags(generics.ListAPIView):
    serializer_class = CommentTagSerializer
    queryset = CommentTag.objects.all()

    def get_queryset(self):
        comment_id_text = self.kwargs["comment_id_text"]
        return CommentTag.objects.filter(comment_id=comment_id_text)
