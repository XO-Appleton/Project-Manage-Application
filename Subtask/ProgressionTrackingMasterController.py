from SubtaskDatabase import SubtaskDatabase
from ProgressionTrackingMainScreen import ProgressionTrackingMainScreen
from DecisionEnum import DecisionEnum
from SubtaskCreator import SubtaskCreator
from SubtaskModifier import SubtaskModifier
from Project import Project
from User import User

class ProgressionTrackingMasterController:

    def main(self, project: Project, user: User):
        ptms = ProgressionTrackingMainScreen()
        sdb = SubtaskDatabase.get_instance()
        
        while True:
            subtasks = sdb.get_subtasks(project.get_uid())
            ptms.display_all_subtasks(subtasks)
            next_op = ptms.get_next_operation()
            if next_op == DecisionEnum.CREATE:
                SubtaskCreator().start_creation(project, user)
            elif next_op == DecisionEnum.MODIFY or next_op == DecisionEnum.TOGGLE or next_op == DecisionEnum.DELETE:
                subtask = ptms.select_subtask()
                SubtaskModifier().start_modification(project, subtask, user, next_op)
            elif next_op == DecisionEnum.VIEW_COMP:
                ptms.view_completion_rate()
            else:
                return