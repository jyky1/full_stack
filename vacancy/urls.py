from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import VecencyView, TeamView, RoleView


router = DefaultRouter()
router.register('vecency', VecencyView)
router.register('team', TeamView)
router.register('role', RoleView)

urlpatterns = [
    path('', include(router.urls))
]