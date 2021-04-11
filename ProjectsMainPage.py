from Project import Project
from OpEnum import OpEnum

class ProjectsMainPage:

    currently_showing = None

    def show_projects(self, projects: list):
        self.currently_showing = projects
        for project in projects:
            print("%d\t%s" % (project.get_uid(), project.name))

    def show_project_details(self, project: Project):
        print(project)

    def get_next_op(self) -> OpEnum:
        choice = input("Select next operation [CREATE/MODIFY/DELETE/VIEW/USE_FEATURE/EXIT]:")
        if choice == "CREATE":
            return OpEnum.CREATE
        if choice == "MODIFY":
            return OpEnum.MODIFY
        if choice == "DELETE":
            return OpEnum.DELETE
        if choice == "VIEW":
            return OpEnum.VIEW
        if choice == "USE_FEATURE":
            return OpEnum.USE_FEATURE
        if choice == "EXIT":
            return OpEnum.EXIT
        print("Cannot recognize your choice, try again")
        return self.get_next_op()

    def get_selected_project(self) -> Project:
        id = int(input("PROJECT ID:"))
        for project in self.currently_showing:
            if project.get_uid() == id:
                return project
