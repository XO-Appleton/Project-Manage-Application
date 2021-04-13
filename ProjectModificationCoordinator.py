from ProjectModificationScreen import ProjectModificationScreen
from ProjectDataBase import ProjectDataBase
from User import User
from Project import Project
from ModEnum import ModEnum


class ProjectCreationCoordinator:

    def __init__(self, user, project):
        self.user = user
        self.current_project = project

    def modify_project(self, user: User, project:Project):
        screen = ProjectModificationScreen()
        self.current_project = screen.initiate_process(self.current_project)
        enum_val = screen.get_mod_type()
        if enum_val == ModEnum.ADD_USER:
            user = User()
            user.login_name = screen.get_user_to_add()
            self.current_project = screen.add_user(user)
        elif enum_val == ModEnum.REMOVE_USER:
            user = User()
            user.login_name = screen.get_user_to_remove()
            self.current_project = screen.remove_user(user)

        elif enum_val == ModEnum.TOGGLE:
            self.current_project = screen.toggle_completion()

    def validate_project(self):
        check_project = self.current_project.__dict__
        project_keys = list(check_project.keys())
        project_values = list(check_project.values())
        for project_input in project_values:
            if (str(project_input).isspace() or str(project_input) == ''):
                blank_input = project_keys[project_values.index(project_input)]
                print("Project is invalid, %s field is blank." %
                      str(blank_input))
                return False

            elif (check_project["date_created"] > check_project["due_date"]):
                print(
                    "Project is invalid, due date cannot be earlier than current date.")
                return False

        return True

    def update_to_system(self, project: Project):
        ProjectDataBase.change_project(project.uid, project)

    def main(self):
        while(True):
            self.modify_project(self.user, self.current_project)
            if (self.validate_project()):
                self.update_to_system(self.current_project)
                print("Success")

            else:
                print("Failure")


if __name__ == "__main__":
    test = User()
    proj = Project()

    test_proj = ProjectCreationCoordinator(test, proj)
    test_proj.main()
