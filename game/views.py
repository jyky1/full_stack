from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, AllowAny

from .serializers import GameSerializer, RatingSerializer
from .models import Game, Rating
from .permissions import IsAuthor


class IsAdminMixin:
    def get_permissions(self):
        if self.action == 'create':
            permissions = [IsAdminUser, ]
        elif self.action in ['update', 'partical_update', 'destroi']:
            permissions = [IsAdminUser,]
        else:
            permissions=[AllowAny,]
        return [permission() for permission in permissions]

class GameView(ModelViewSet):
    serializer_class = GameSerializer
    queryset = Game.objects.all()

class UserPermissionMixin:
    def get_permissions(self):
        if self.action == 'create':
            permissions = [IsAuthor, ]
        elif self.action in ['update', 'partical_update', 'destroi']:
            permissions = [IsAuthor,]
        else:
            permissions=[AllowAny,]
        return [permission() for permission in permissions]

class RatingView(UserPermissionMixin ,ModelViewSet):
    serializer_class = RatingSerializer
    queryset = Rating.objects.all()