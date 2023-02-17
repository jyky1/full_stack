from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, AllowAny

from .serializers import TeamSerializer, RoleSerialize, VacancySerializer
from .models import Team, Role, Vacancy


class TeamView(IsAdminUser, ModelViewSet):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()


class RoleView(IsAdminUser, ModelViewSet):
    serializer_class = RoleSerialize
    queryset = Role.objects.all()


class VecencyView(IsAdminUser, ModelViewSet):
    serializer_class = VacancySerializer
    queryset = Vacancy.objects.all()

    