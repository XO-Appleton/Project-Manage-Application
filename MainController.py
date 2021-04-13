from User import User
from Project import Project
from LoginCoordinator import LoginCoordinator
from ProjectCreationCoordinator import ProjectCreationCoordinator
from ProjectModificationCoordinator import ProjectModificationCoordinator
from ProjectDeleteCoordinator import ProjectDeleteCoordinator
from FeatureSelector import FeatureSelector
from ProjectsMainPage import ProjectsMainPage
from CredentialDatabase import CredentialDatabase
from ProjectDataBase import ProjectDataBase
from OpEnum import OpEnum

class MainController:
    
    def initialize(self):
        self.cdb = CredentialDatabase.get_instance()
        self.pdb = ProjectDataBase.get_instance()

        self.pmp = ProjectsMainPage()

        self.lc = LoginCoordinator()
        self.pcc = ProjectCreationCoordinator()
        self.pmc = ProjectModificationCoordinator()
        self.pdc = ProjectDeleteCoordinator()
        self.fs = FeatureSelector()

    def main(self):
        self.initialize()
        self.current_user = self.lc.start_login_process()
        self.involved_projects = self.pdb.get_user_projects(self.current_user)

        keep_running = True
        while keep_running:
            self.pmp.show_projects(self.involved_projects)
            next_op = self.pmp.get_next_op()
            if next_op == OpEnum.CREATE:
                self.pcc.create_new_project(self.current_user)
            elif next_op == OpEnum.MODIFY:
                project_to_modify = self.pmp.get_selected_project()
                self.pmc.modify_project(project_to_modify, self.current_user)
            elif next_op == OpEnum.DELETE:
                project_to_delete = self.pmp.get_selected_project()
                self.pdc.delete_project(project_to_delete, self.current_user)
            elif next_op == OpEnum.VIEW:
                project_to_view = self.pmp.get_selected_project()
                self.pmp.show_project_details(project_to_view)
            elif next_op == OpEnum.USE_FEATURE:
                project_for_feature = self.pmp.get_selected_project()
                self.fs.start_branch_usage(project_for_feature, self.current_user)
            else:
                self.terminate()
                return
            self.involved_projects = self.pdb.get_user_projects(self.current_user)

    def terminate(self):
        self.cdb.save_database()
        self.pdb.save_database()


if __name__ == "__main__":
    MainController().main()