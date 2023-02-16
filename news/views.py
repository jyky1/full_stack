from django.shortcuts import render
from models import News, Comment, Like
from rest_framework import viewsets, generics
from serializers import NewsSerializer, CommentSerializer, LikeSerializer
from rest_framework.permissions import IsAdminUser




class NewsViewSet(IsAdminUser,viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class CommentView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class LikeView(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer



    

