from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import GameView


router = DefaultRouter()
router.register('game', GameView)

urlpatterns = [
    path('', include(router.urls))
]