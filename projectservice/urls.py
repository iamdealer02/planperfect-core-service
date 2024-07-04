from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectServiceViewSet, ProjectTeamServiceViewSet, ProjectTasksServiceViewSet

router = DefaultRouter()
router.register(r'projects', ProjectServiceViewSet, basename='projectservice')
router.register(r'teams', ProjectTeamServiceViewSet, basename='projectteamservice')
router.register(r'tasks', ProjectTasksServiceViewSet, basename='projecttasksservice')

urlpatterns = [
    path('', include(router.urls)),
    path('task/<str:project_id>/create/', ProjectTasksServiceViewSet.as_view({'post': 'create_task'}), name='create_task'),
    path('task/<str:project_id>/tasks/', ProjectTasksServiceViewSet.as_view({'get': 'list_tasks'}), name='list_tasks'),
    path('task/<str:project_id>/tasks/<str:task_id>/', ProjectTasksServiceViewSet.as_view({'get': 'get_task'}), name='view_task'),
    path('task/<str:project_id>/tasks/<str:task_id>/update/', ProjectTasksServiceViewSet.as_view({'patch': 'update_task'}), name='update_task'),
    path('task/<str:project_id>/tasks/<str:task_id>/delete/', ProjectTasksServiceViewSet.as_view({'delete': 'delete_task'}), name='delete_task'),
]
