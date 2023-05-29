from rest_framework.response import Response
from rest_framework.decorators import api_view
from social.models import User, Post, Comment, Tag, Follower, PostLikes, CommentLikes, UserFollowsTag
from .serializers import UserSerializer, PostSerializer, CommentSerializer, TagSerializer, FollowerSerializer, PostLikesSerializer, CommentLikesSerializer, tagfollowserializer
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
class DeletePost(generics.DestroyAPIView):
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

class UnlikePost(generics.DestroyAPIView):
    model = PostLikes
    serializer_class = PostLikesSerializer
    def get_object(self, queryset=None):
        return PostLikes.objects.get(post_likes_id_text=self.kwargs.get("post_likes_id_text"))


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

    def comment(self, request, *args, **kwargs):
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


@api_view(['GET'])
def getData(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addUser(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def updateData(request):
    users = User.objects.get(UserID=request.data['user_id_bin'])
    serializer = UserSerializer(request, data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view
def deleteUser(request):
    users = User.objects.get(UserID = request.data)
    users.delete()
    return Response()