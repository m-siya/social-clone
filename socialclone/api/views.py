from rest_framework.response import Response
from rest_framework.decorators import api_view
from social.models import User, Post, Comment, Tag, Follower, PostLikes
from .serializers import UserSerializer, PostSerializer, CommentSerializer, TagSerializer, FollowerSerializer, PostLikesSerializer
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
class LikeUnlikePost(generics.CreateAPIView, generics.DestroyAPIView):
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
            self.perform_destroy(existing_like)
            return Response({'detail': 'Post unliked successfully.'})
        else:
            # If the user has not liked the post, create a new like
            return self.create(request, *args, **kwargs)
        
# follower views
# add follower, remove follower, view all follower, view all following
#view all entries
# class FollowerList(generics.ListAPIView):
#     queryset = Follower.objects.all()
#     serializer_class = FollowerSerializer

# add and remove follower
class AddRemoveFollower(generics.CreateAPIView, generics.DestroyAPIView):
    serializer_class = FollowerSerializer

    def get_queryset(self):
        user_id = self.request.data.get('user')
        follower_id = self.request.data.get('follower')
        return Follower.objects.filter(user=user_id, follower=follower_id)

    def post(self, request, *args, **kwargs):
        # Check if the follower has already followed the user
        existing_follower = self.get_queryset().first()

        if existing_follower:
            # If the user has already followed, remove 
            self.perform_destroy(existing_follower)
            return Response({'detail': 'User unfollowed successfully.'})
        else:
            # If the user has not followed, create a new follower
            return self.create(request, *args, **kwargs)

# view all followers
class Followers(generics.ListCreateAPIView):
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer

    # def get_queryset(self):
    #     user_id_text = self.kwargs["user_id_text"]
    #     user = User.objects.get(user_id_text=user_id_text)
    #     return Follower.objects.filter(user = user).exclude(follower = user)


    
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