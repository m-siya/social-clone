from rest_framework.response import Response
from rest_framework.decorators import api_view
from social.models import User
from .serializers import UserSerializer
from rest_framework import generics

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    model = User
    serializer_class = UserSerializer
    def get_object(self, queryset=None):

        return User.objects.get(user_id_text=self.kwargs.get("user_id_text"))

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