from rest_framework import serializers

from .models import Team, Role, Vacancy

class TeamSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Team
        fields = '__all__'



class RoleSerialize(serializers.ModelSerializer):


    class Meta:
        model = Role
        fields = '__all__'


class VacancySerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Vacancy
        fields = '__all__'