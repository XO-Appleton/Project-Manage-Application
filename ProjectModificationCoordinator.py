from ProjectModificationScreen import ProjectModificationScreen
from ProjectDataBase import ProjectDataBase
from User import User
from Project import Project
from ModEnum import ModEnum
from CredentialDatabase import CredentialDatabase


class ProjectModificationCoordinator:

    def __init__(self):
        pass

    def modify_project(self, project: Project, user: User):
        screen = ProjectModificationScreen()
        self.current_project = project
        screen.initiate_process(self.current_project)
        enum_val = screen.get_mod_type()
        if enum_val == ModEnum.ADD_USER:
            if not user.get_user_ID() == self.current_project.get_admin().get_user_ID():
                print("You are not the admin, access denied.")
                return
            user_name = screen.get_user_to_add()
            new_user = CredentialDatabase.get_instance().get_user_from_login_name(user_name)
            print("Adding user %s %d" % (new_user.first_name, new_user.user_ID))
            self.current_project = screen.add_user(new_user)

        elif enum_val == ModEnum.REMOVE_USER:
            if not user.get_user_ID() == project.get_admin().get_user_ID():
                print("You are not the admin, access denied.")
                return
            user_name = screen.get_user_to_remove()
            removed_user = CredentialDatabase.get_instance().get_user_from_login_name(user_name)
            self.current_project = screen.remove_user(removed_user.get_login_name())
        elif enum_val == ModEnum.TOGGLE:
            self.current_project = screen.toggle_completion()

        self.update_to_system(self.current_project)

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
        ProjectDataBase.get_instance().change_project(project.uid, project)

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
