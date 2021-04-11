from Project import Project
from User import User
from ModEnum import ModEnum

class ProjectModificationScreen:

    project_on_modify : Project = None

    def initiate_process(self, project: Project):
        self.project_on_modify = project

    def get_mod_type(self) -> ModEnum:
        choice = input("Please choose mod operation [ADD_USER/REMOVE_USER/TOGGLE]:")
        if choice == "ADD_USER":
            return ModEnum.ADD_USER
        if choice == "REMOVE_USER":
            return ModEnum.REMOVE_USER
        if choice == "TOGGLE":
            return ModEnum.TOGGLE
        print("Cannot recognize choice, please try again")
        return self.get_mod_type()

    def get_user_to_add(self) -> str:
        return input("LOGIN NAME OF ADDED USER:")

    def add_user(self, user: User) -> Project:
        if user.get_login_name() not in [u.get_login_name() for u in self.project_on_modify.member]:
            self.project_on_modify.member.append(user)
        return self.project_on_modify

    def get_user_to_remove(self) -> str:
        return input("LOGIN NAME OF REMOVED USER:")

    def remove_user(self, user_login_name: str):
        for i in range(len(self.project_on_modify.member)):
            if self.project_on_modify.member[i].get_login_name() == user_login_name:
                self.project_on_modify.member.pop(i)
                break
        return self.project_on_modify