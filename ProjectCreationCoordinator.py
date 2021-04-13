from ProjectCreationScreen import ProjectCreationScreen
from ProjectDataBase import ProjectDataBase
from User import User
from Project import Project


class ProjectCreationCoordinator:

    def __init__(self, user):
        self.user = user
        self.current_project = None
        self.active = True

    def create_new_project(self, user: User):
        self.current_project = ProjectCreationScreen().display_form(user)

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

    def add_to_system(self, project: Project):
        ProjectDataBase().add_project(project)

    def main(self):
        while(self.active):
            self.create_new_project(self.user)
            if (self.validate_project()):
                self.add_to_system(self.current_project)
                print("Project creation complete.")
                self.active = False

            else:
                print("Exiting Project Creation")
                self.active = False


if __name__ == "__main__":
    test = User()
    test.login_name = "hat"
    test_project = ProjectCreationCoordinator(test)
    test_project.main()
