from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .serializers import ResumeSerializer
from .models import Resume


class ResumeView(ModelViewSet):
    queryset=Resume.objects.all()
    serializer_class=ResumeSerializer