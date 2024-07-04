from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import ProjectServiceSerializer
from .models import ProjectService
from .connector import ProjectServiceConnector, ProjectTeamServiceConnector
from django.urls import path
from rest_framework.decorators import action

class ProjectServiceViewSet(viewsets.ModelViewSet):
    queryset = ProjectService.objects.all()
    serializer_class = ProjectServiceSerializer
    
    def create(self, request, *args, **kwargs):
        connector = ProjectServiceConnector()
        headers = dict(request.headers)
        response = connector.create_project(request.data, headers)
        return self.handle_response(response)

    def list(self, request, *args, **kwargs):
        connector = ProjectServiceConnector()
        headers = dict(request.headers)
        response = connector.get_projects(headers)
        return self.handle_response(response)
    
    def retrieve(self, request, pk=None):
        connector = ProjectServiceConnector()
        headers = dict(request.headers)
        response = connector.get_project(pk, headers)
        return self.handle_response(response)
    
    def update(self, request, pk=None):
        connector = ProjectServiceConnector()
        headers = dict(request.headers)
        response = connector.update_project(pk, request.data, headers)
        return self.handle_response(response)
    
    def destroy(self, request, pk=None):
        connector = ProjectServiceConnector()
        headers = dict(request.headers)
        response = connector.delete_project(pk, headers)
        return Response(status=response.status_code, data=response.json())

    def handle_response(self, response):
        try:
            return Response(response.json(), status=response.status_code)
        except ValueError:
            return Response({'message': 'Invalid response format'}, status=response.status_code)

class ProjectTeamServiceViewSet(viewsets.ModelViewSet):
    queryset = ProjectService.objects.all()
    serializer_class = ProjectServiceSerializer

    def create(self, request, *args, **kwargs):
        connector = ProjectTeamServiceConnector()
        headers = dict(request.headers)
        response = connector.create_project_team(request.data, headers)
        return self.handle_response(response)
    
    def list(self, request, *args, **kwargs):
        connector = ProjectTeamServiceConnector()
        headers = dict(request.headers)
        response = connector.get_all_user_projects(headers)
        return self.handle_response(response)
    
    def retrieve(self, request, pk=None):
        connector = ProjectTeamServiceConnector()
        headers = dict(request.headers)
        response = connector.get_project_team(pk, headers)
        return self.handle_response(response)
    
    @action(detail=True, methods=['put'] ,url_path='update-member/(?P<member_id>[^/.]+)')
    def update_member(self, request, pk=None, member_id=None):
        connector = ProjectTeamServiceConnector()
        headers = dict(request.headers)
        response = connector.update_project_team(pk, member_id, request.data, headers)
        return self.handle_response(response)
    @action(detail=True, methods=['delete'], url_path='delete-member/(?P<member_id>[^/.]+)')
    def delete_member(self, request, pk=None, member_id=None):
        connector = ProjectTeamServiceConnector()
        headers = dict(request.headers)
        response = connector.delete_project_team(pk, member_id, headers)
        return Response(status=response.status_code, data=response.json())
    
    def handle_response(self, response):
        try:
            return Response(response.json(), status=response.status_code)
        except ValueError:
            return Response({'message': 'Invalid response format', 'error': str(response)}, status=response.status_code)
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('<pk>/update-member/<mid>/', self.update_member, name='team-update-member'),
            path('<pk>/delete-member/<mid>/', self.delete_member, name='team-delete-member'),
        ]
        return urls + custom_urls 