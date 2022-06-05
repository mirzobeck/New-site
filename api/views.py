from django.shortcuts import render
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from .serializers import postserializers, userserializers
from blog.models import post
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly
from .permissions import IsAuthorOrReadOnly
from rest_framework import viewsets

class postsviewset(viewsets.ModelViewSet):
    queryset = post.published.all()
    serializer_class = postserializers

class userviewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = userserializers


# class postlistapi(ListAPIView):
#     queryset = post.published.all()
#     serializer_class = postserializers
#     permission_classes = [IsAdminUser]


# class postcreateapi(CreateAPIView):
#     queryset = post.published.all()
#     serializer_class = postserializers
#     permission_classes = (IsAuthenticatedOrReadOnly,)


# class retrieveapi(RetrieveUpdateDestroyAPIView):
#     queryset = post.published.all()
#     serializer_class = postserializers
#     permission_classes = [IsAuthorOrReadOnly]
