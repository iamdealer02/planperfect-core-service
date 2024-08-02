from django.urls import path
from .views import RegisterUserView, LoginUserView, UserServiceViewSet

urlpatterns = [
    path('register/', RegisterUserView.as_view({'post': 'create'}), name='register_user'),
    path('login/', LoginUserView.as_view({'post': 'create'}), name='login_user'),
    path('ping/', UserServiceViewSet.as_view({'get': 'get'}), name='ping_user_service'),
]

