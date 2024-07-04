from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import ProjectServiceSerializer
from .models import ProjectService
from .connector import ProjectServiceConnector

class ProjectServiceViewSet(viewsets.ModelViewSet):
    queryset = ProjectService.objects.all()
    serializer_class = ProjectServiceSerializer
    
    def create(self, request, *args, **kwargs):
        # Create a connector instance
        connector = ProjectServiceConnector()
        
        # Extract headers
        headers = dict(request.headers)
        
        # Create project
        response = connector.create_project(request.data, headers)
        return self.handle_response(response)

    def list(self, request, *args, **kwargs):
        # Create a connector instance
        connector = ProjectServiceConnector()
        
        # Extract headers
        headers = dict(request.headers)
        
        # Get projects
        response = connector.get_projects(headers)
        return self.handle_response(response)
    
    def retrieve(self, request, pk=None):
        # Create a connector instance
        connector = ProjectServiceConnector()
        
        # Extract headers
        headers = dict(request.headers)
        
        # Get project
        response = connector.get_project(pk, headers)
        return self.handle_response(response)
    
    def update(self, request, pk=None):
        # Create a connector instance
        connector = ProjectServiceConnector()
        
        # Extract headers
        headers = dict(request.headers)
        
        # Update project
        response = connector.update_project(pk, request.data, headers)
        return self.handle_response(response)
    
    def destroy(self, request, pk=None):
        # Create a connector instance
        connector = ProjectServiceConnector()
        
        # Extract headers
        headers = dict(request.headers)
        
        # Delete project
        response = connector.delete_project(pk, headers)
        return Response(status=response.status_code, data=response.json())

    def handle_response(self, response):
        try:
            return Response(response.json(), status=response.status_code)
        except ValueError:
            return Response({'message': 'Invalid response format'}, status=response.status_code)
