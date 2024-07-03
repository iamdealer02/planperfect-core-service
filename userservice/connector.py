import requests

class UserServiceConnector:
    def __init__(self):
        self.url = 'http://userservice-backend-1:8000/user/'

    def send_ping(self, endpoint:str):
        response = requests.get(url=endpoint)

        if response.status_code == 200:
            return True
        else:
            return False 
    # registering users /users/register
    def register_user(self, data):
        response = requests.post(url=self.url+'register/', data=data)
        return response
    
    def login_user(self, data):
        response = requests.post(url=self.url+'login/', data=data)
        return response
    
    