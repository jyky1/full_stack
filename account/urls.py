from django.urls import path
from .views import ChangePasswordView, ForgotPasswordCompleteView, ForgotPasswordView, RegisterView, ActivationView, LogoutView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import ChangePasswordView, ForgotPasswordCompleteView, ForgotPasswordView, RegisterView, ActivationView, LogoutView


urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('activate/<str:email>/<str:activation_code>/', ActivationView.as_view(), name='activate'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view(), name='auth_logout'),
    path('change_password/', ChangePasswordView.as_view()),
    path('forgot_password/',  ForgotPasswordView.as_view()),
    path('forgot_password_complete/', ForgotPasswordCompleteView.as_view()),
]

