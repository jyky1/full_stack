from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.pagination import PageNumberPagination

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

    

class LargeResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10


class ResumeView(UserPermissionMixin, ModelViewSet):
    queryset=Resume.objects.all()
    serializer_class = ResumeSerializer
    pagination_class = LargeResultsSetPagination