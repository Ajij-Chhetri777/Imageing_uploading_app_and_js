from django.shortcuts import render
from api.serializers import Thepostserializer, CommentSerializer, TypeSerializer
from rest_framework import generics
from theapp.models import Thepost, Comment, Type
from rest_framework import response
from rest_framework.views import APIView
from rest_framework import permissions
# Create your views here.
class ThepostAPI(generics.ListCreateAPIView):
    queryset = Thepost.objects.all()
    serializer_class = Thepostserializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = "title"

class CommentAPI(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class postviewAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Thepost.objects.all()
    serializer_class = Thepostserializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CommentviewByPostAPI(generics.ListAPIView):
    def get_queryset(self):
        return Thepost.objects.get(id = self.kwargs['pk']).belongs.all()
    serializer_class = CommentSerializer 

class TypeviewByUserAPI(generics.ListAPIView):
    def get_queryset(self):
        return  Type.objects.get(id = self.kwargs['pk']).types.all()
    serializer_class = Thepostserializer
    