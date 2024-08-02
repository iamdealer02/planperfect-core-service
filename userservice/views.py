from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import UserServiceSerializer
from .models import UserService
from .connector import UserServiceConnector

class UserServiceViewSet(viewsets.ModelViewSet):
    queryset = UserService.objects.all()
    serializer_class = UserServiceSerializer
    
    def get(self, request, *args, **kwargs):
        # Extract the request path
        endpoint = request.path
        
        # Check if the endpoint exists in UserService
        current_service = UserService.objects.filter(endpoint=endpoint).first()

        if not current_service:
            return Response({'message': 'Service not found!'}, status=status.HTTP_404_NOT_FOUND)
        
        # Create a connector instance
        connector = UserServiceConnector()

        # Example of checking if the user service is up and running
        if not connector.send_ping(connector.url):
            return Response({'message': 'User service is down'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)

        return Response({'message': 'User service is up and running'}, status=status.HTTP_200_OK)

class RegisterUserView(viewsets.ViewSet):
    def create(self, request, *args, **kwargs):
        # Create a connector instance
        connector = UserServiceConnector()
        
        # Register user
        response = connector.register_user(request.data)
        return Response(response.json(), status=response.status_code)
        
class LoginUserView(viewsets.ViewSet):
    def create(self, request, *args, **kwargs):
        # Create a connector instance
        connector = UserServiceConnector()
        
        # Log in user
        response = connector.login_user(request.data)
        return Response(response.json(), status=response.status_code)
