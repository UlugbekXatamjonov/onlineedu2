from django.urls import path, include

from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView, TokenBlacklistView
from rest_framework.routers import DefaultRouter
from .views import UserRegistrationView, UserLoginView, UserProfileView, UserChangePasswordView, \
    SendPasswordResetEmailView, UserPasswordResetView, LogoutAPIView


app_name = 'student'


router = DefaultRouter()
# router.register(r'contact', ContactViewset, 'contact')
# router.register(r'student', StudentViewset, 'student')
router.register(r'profile', UserProfileView, 'profile')

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name="registration"),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', UserLoginView.as_view(), name="login"),
    path('logout/', LogoutAPIView.as_view(), name="logout"),
    # path('api/token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),

    path('change-password/', UserChangePasswordView.as_view(), name="change_password"),
    path('send-reset-password-email/', SendPasswordResetEmailView.as_view(), name="send_reset_password_email"),
    path('reset-password/<uid>/<token>/', UserPasswordResetView.as_view(), name='reset-password'),

    path('', include(router.urls))
]




