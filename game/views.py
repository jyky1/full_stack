from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .serializers import GameSerializer, RatingSerializer
from .models import Game, Rating

class GameView(ModelViewSet):
    serializer_class = GameSerializer
    queryset = Game.objects.all()


class RatingView(ModelViewSet):
    serializer_class = RatingSerializer
    queryset = Rating.objects.all()