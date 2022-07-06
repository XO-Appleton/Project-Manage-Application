from datetime import date

from Project import Project
from User import User
from Subtask import Subtask
from SubtaskCreationScreen import SubtaskCreationScreen
from SubtaskDatabase import SubtaskDatabase

class SubtaskCreator:

    def start_creation(self, project: Project, user: User):
        scs = SubtaskCreationScreen()
        subtask = scs.get_input(project.is_admin(user))
        if self.validate(subtask, project, user):
            print("Adding subtask %s" % subtask.name)
            SubtaskDatabase.get_instance().add_subtask(project.get_uid(), subtask)
        else:
            print("INVALID SUBTASK, aborting...")

    def validate(self, subtask: Subtask, project: Project, user: User) -> bool:
        if not project.get_admin().get_user_ID() == user.get_user_ID():
            if not subtask.modifiable or not subtask.removable:
                print("You are NOT privileged!")
                return False
        if not subtask.due >= date.today():
            print("Cannot due in the past!")
            return False
        if not any([c.isalnum() for c in subtask.name]):
            print("Invalid name!")
            return False
        return True