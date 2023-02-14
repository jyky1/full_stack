from django.urls import path
from .views import RegisterView, ActivationView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('activate/<str:email>/<str:activation_code>/', ActivationView.as_view(), name='activate'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]


# from django.urls import path, include
# from .views import RegisterView, ActivationView
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('rating', RegisterView)
# router.register('comments', ActivationView)

# urlpatterns = [
#     path('',  include(router.urls)),
# ]