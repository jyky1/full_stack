from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from .serializers import ResumeSerializer
from .models import Resume
from .permissions import IsAuthor

class UserPermissionMixin:
    def get_permissions(self):
        if self.action == 'create':
            permissions = [IsAuthor, ]
        elif self.action in ['update', 'partical_update', 'destroi']:
            permissions = [IsAuthor,]
        else:
            permissions=[AllowAny,]
        return [permission() for permission in permissions]

class ResumeView(UserPermissionMixin, ModelViewSet):
    queryset=Resume.objects.all()
    serializer_class=ResumeSerializer