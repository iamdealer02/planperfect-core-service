from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectServiceViewSet, ProjectTeamServiceViewSet

router = DefaultRouter()
router.register(r'projects', ProjectServiceViewSet, basename='projectservice')
router.register(r'teams', ProjectTeamServiceViewSet, basename='projectteamservice')

urlpatterns = [
    path('', include(router.urls)),
]
