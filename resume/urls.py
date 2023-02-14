from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ResumeView


router = DefaultRouter()
router.register('resume', ResumeView)

urlpatterns = [
    path('', include(router.urls))
]