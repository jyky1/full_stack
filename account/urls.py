from django.urls import path
from .views import OrderView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView