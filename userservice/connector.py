import requests

class UserServiceConnector:
    service_url = None

    def __init__(self):
        if not UserServiceConnector.service_url:
            response = requests.get('http://servicediscovery-backend-1:8003/service/discover/userservice').json()
            UserServiceConnector.service_url = response['address']
        
        self.url = UserServiceConnector.service_url + 'user/'

    def send_ping(self, endpoint: str):
        response = requests.get(url=endpoint)
        return response.status_code == 200

    def register_user(self, data):
        response = requests.post(url=self.url + 'register/', data=data)
        return response

    def login_user(self, data):
        print(self.url)
        response = requests.post(url=self.url + 'login/', data=data)
        return response
