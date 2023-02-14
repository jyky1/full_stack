from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .serializers import GameSerializer
from .models import Game

class GameView(ModelViewSet):
    serializer_class=GameSerializer
    queryset=Game.objects.all()
    