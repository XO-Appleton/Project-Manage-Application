from datetime import date

from Project import Project
from Subtask import Subtask
from User import User
from DecisionEnum import DecisionEnum
from SubtaskDatabase import SubtaskDatabase
from SubtaskModificationScreen import SubtaskModificationScreen

class SubtaskModifier:

    def start_modification(self, project: Project, subtask: Subtask, user: User, decision: DecisionEnum):
        sdb = SubtaskDatabase.get_instance()
        if decision == DecisionEnum.MODIFY:
            if self.can_modify(project, subtask, user):
                sms = SubtaskModificationScreen()
                sms.display_form(subtask)
                modified_subtask = sms.get_input(project.is_admin(user))
                if self.validate(modified_subtask, project, user):
                    sdb.modify_subtask(project.get_uid(), modified_subtask)
        elif decision == DecisionEnum.TOGGLE:
            sdb.toggle_subtask(project.get_uid(), subtask.uid)
        elif decision == DecisionEnum.DELETE:
            if self.can_delete(project, subtask, user):
                sdb.remove_subtask(project.get_uid(), subtask.uid)

    def can_delete(self, project: Project, subtask: Subtask, user: User) -> bool:
        if not self.is_admin(project, user):
            return subtask.removable
        return True

    def can_modify(self, project: Project, subtask: Subtask, user: User) -> bool:
        if not self.is_admin(project, user):
            return subtask.modifiable
        return True

    def validate(self, subtask: Subtask, project: Project, user: User) -> bool:
        if not project.get_admin().get_user_ID() == user.get_user_ID():
            if not subtask.modifiable or not subtask.removable:
                print("You are NOT privileged!")
                return False
        return subtask.due >= date.today() and subtask.name.isalnum()

    def is_admin(self, project: Project, user: User):
        return project.get_admin().get_user_ID() == user.get_user_ID()