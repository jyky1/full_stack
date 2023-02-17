from django.urls import include, path
from rest_framework import routers

from .views import NewsViewSet, CommentView, LikeView

router = routers.DefaultRouter()
router.register('news', NewsViewSet)
router.register('likes', LikeView)
router.register('comments', CommentView)

urlpatterns = [
    path('', include(router.urls)),
]