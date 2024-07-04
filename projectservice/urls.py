from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectServiceViewSet

# Create a router and register the viewset
router = DefaultRouter()
router.register(r'projects', ProjectServiceViewSet)

# Include the router URLs in the urlpatterns
urlpatterns = [
    path('', include(router.urls)),
]
