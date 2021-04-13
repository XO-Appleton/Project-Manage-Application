from ProjectDataBase import *

class ProjectDeleteCoordinator:

    def __init__(self) -> None:
        self.database = ProjectDataBase()
    
    def delete_project(self, project: Project, user: User) -> None:
        if User != Project.get_admin:
            self.failure_to_verify()
            return
        
        confirmation = input('Are you sure you want to delete Project {}? (y/n)'.format(project.get_uid)).upper()
        
        if confirmation == 'Y':
            self.delete_from_system(project)
            return
        else:
            print('Deletion has been cancelled.')
            return

    def delete_from_system(self, project: Project) -> None:
        self.database.delete_project(project)

    @staticmethod
    def failure_to_verify() -> None:
        print('Sorry, only the project admin is privileged to delete a project.')