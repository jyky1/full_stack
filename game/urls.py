from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import GameView, RatingView


router = DefaultRouter()
router.register('game', GameView)
router.register('rating', RatingView)

urlpatterns = [
    path('', include(router.urls))
]