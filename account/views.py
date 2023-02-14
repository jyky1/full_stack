from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import User
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response



class RegisterView(APIView):

    @swagger_auto_schema(request_body=UserSerializer())
    def post(self, request):
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response('Successfully registered', 201)

class ActivationView(APIView):

    def get(self, request, email, activation_code):
        user = User.objects.filter(email=email, activation_code=activation_code,).first()
        if not user:
            return Response('User does not exist', 400)
        user.activation_code = ''
        user.is_active = True
        user.save()
        return Response('Activated', 200)
