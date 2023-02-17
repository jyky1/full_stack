from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser

from .serializers import NewsSerializer, CommentSerializer, LikeSerializer
from .models import News, Comment, Like



class NewsViewSet(IsAdminUser,ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class CommentView(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class LikeView(ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer