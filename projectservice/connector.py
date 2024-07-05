import requests

class ProjectServiceConnector:
    service_url = None

    def __init__(self):
        if not ProjectServiceConnector.service_url:
            ProjectServiceConnector.service_url = requests.get('http://servicediscovery-backend-1:8003/service/discover/projectservice').json()['address']
        self.url = ProjectServiceConnector.service_url + 'api/projects/'

    def send_ping(self, endpoint: str, headers: dict):
        response = requests.get(url=endpoint, headers=headers)
        return response.status_code == 200

    # CRUD for projects
    def create_project(self, data, headers: dict):
        headers.update({'Content-Type': 'application/json'})
        response = requests.post(url=self.url, json=data, headers=headers)
        return response

    def get_projects(self, headers: dict):
        response = requests.get(url=self.url, headers=headers)
        return response

    def get_project(self, project_id, headers: dict):
        response = requests.get(url=self.url + str(project_id) + '/', headers=headers)
        return response

    def update_project(self, project_id, data, headers: dict):
        headers.update({'Content-Type': 'application/json'})
        response = requests.put(url=self.url + str(project_id) + '/', json=data, headers=headers)
        return response

    def delete_project(self, project_id, headers: dict):
        response = requests.delete(url=self.url + str(project_id) + '/', headers=headers)
        return response



class ProjectTeamServiceConnector:
    service_url = None

    def __init__(self):
        if not ProjectTeamServiceConnector.service_url:
            ProjectTeamServiceConnector.service_url = requests.get('http://servicediscovery-backend-1:8003/service/discover/projectservice').json()['address']
        self.url = ProjectTeamServiceConnector.service_url + 'api/teams/'

    def send_ping(self, endpoint: str, headers: dict):
        response = requests.get(url=endpoint, headers=headers)
        return response.status_code == 200

    # CRUD for project teams
    def create_project_team(self, data, headers: dict):
        headers.update({'Content-Type': 'application/json'})
        response = requests.post(url=self.url, json=data, headers=headers)
        return response

    def get_all_user_projects(self, headers: dict):
        response = requests.get(url=self.url, headers=headers)
        return response

    def get_project_team(self, project_team_id, headers: dict):
        response = requests.get(url=self.url + str(project_team_id) + '/', headers=headers)
        return response

    def update_project_team(self, project_team_id, member_id, data, headers: dict):
        headers.update({'Content-Type': 'application/json'})
        response = requests.put(url=self.url + str(project_team_id) + '/update-member/' + str(member_id) + '/', json=data, headers=headers)
        return response

    def delete_project_team(self, project_team_id, member_id, headers: dict):
        response = requests.delete(url=self.url + str(project_team_id) + '/delete-member/' + str(member_id) + '/', headers=headers)
        return response
    


class ProjectTasksServiceConnector:
    service_url = None

    def __init__(self):
        if not ProjectTasksServiceConnector.service_url:
            ProjectTasksServiceConnector.service_url = requests.get('http://servicediscovery-backend-1:8003/service/discover/projectservice').json()['address']
        self.url = ProjectTasksServiceConnector.service_url

    def send_ping(self, endpoint: str, headers: dict):
        response = requests.get(url=endpoint, headers=headers)
        return response.status_code == 200

    # custom CRUD for project tasks
    def get_project_tasks(self, project_id, headers: dict):
        response = requests.get(url=self.url + '/' + str(project_id) + '/tasks/', headers=headers)
        return response

    def create_project_task(self, project_id, data, headers: dict):
        headers.update({'Content-Type': 'application/json'})
        response = requests.post(url=self.url + '/' + str(project_id) + '/create/', json=data, headers=headers)
        return response

    def get_project_task(self, project_id, task_id, headers: dict):
        response = requests.get(url=self.url + '/' + str(project_id) + '/tasks/' + str(task_id) + '/', headers=headers)
        return response

    def update_project_task(self, project_id, task_id, data, headers: dict):
        headers.update({'Content-Type': 'application/json'})
        response = requests.patch(url=self.url + '/' + str(project_id) + '/tasks/' + str(task_id) + '/update/', json=data, headers=headers)
        return response

    def delete_project_task(self, project_id, task_id, headers: dict):
        response = requests.delete(url=self.url + '/' + str(project_id) + '/tasks/' + str(task_id) + '/delete/', headers=headers)
        return response
