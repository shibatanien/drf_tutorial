from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Drink
from .serializers import DrinkSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from .permissions import IsOwnerOrReadOnly

class DrinkList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer
    

class DrinkDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer
    
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
