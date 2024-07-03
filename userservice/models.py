from django.db import models

# Define the UserService model
class UserService(models.Model):
    endpoint = models.CharField(max_length=100, null=True, default=None)
    last_communication = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.endpoint
