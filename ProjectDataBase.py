from User import User
from Project import Project


class ProjectDataBase:

    def add_project(self, project: Project):
        pass

    def change_project(self, project_id: int, project: Project):
        pass

    def delete_project(self, project_id: int):
        pass

    def get_project(self, project_id: int):
        pass

    def get_user_projects(self, user: User) -> list:
        pass

    @staticmethod
    def get_instance():
        pass
