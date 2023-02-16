from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.viewsets import ModelViewSet
from .models import Company
from .serializers import CompanySerializer




class IsAdminMixin:

    def get_permissions(self):
        if self.action == 'create':
            permissions = [IsAdminUser, ]
        elif self.action in ['update', 'partical_update', 'destroi']:
            permissions = [IsAdminUser,]
        else:
            permissions=[AllowAny,]
        return [permission() for permission in permissions]


class CompanyViewSet(IsAdminMixin, ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer