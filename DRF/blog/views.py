from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.authentication import TokenAuthentication
from .models import Post, Comment
from .serializer import PostSerializer, CommentSerializer

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    permissions_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [TokenAuthentication]

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
