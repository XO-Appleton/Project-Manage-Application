from ProjectDataBase import *

class ProjectDeleteCoordinator:

    def __init__(self) -> None:
        self.database = ProjectDataBase.get_instance()
    
    def delete_project(self, project: Project, user: User) -> None:
        if user.get_user_ID() != project.get_admin().get_user_ID():
            self.failure_to_verify()
            return
        
        confirmation = input('Are you sure you want to delete Project {}? (y/n)'.format(project.get_uid())).upper()
        
        if confirmation == 'Y':
            self.delete_from_system(project)
            return
        else:
            print('Deletion has been cancelled.')
            return

    def delete_from_system(self, project: Project) -> None:
        self.database.delete_project(project.get_uid())

    @staticmethod
    def failure_to_verify() -> None:
        print('Sorry, only the project admin is privileged to delete a project.')