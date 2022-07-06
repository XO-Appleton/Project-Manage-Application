import Subtask
from DecisionEnum import DecisionEnum


class ProgressionTrackingMainScreen:

    def __init__(self):
        self.displayed_subtasks: list = None

    def display_all_subtasks(self, subtasks: list):
        self.displayed_subtasks = subtasks
        print("Involved subtasks:")
        print("%-10s %-20s %-10s %-10s %-10s %-10s" % ("ID", "NAME", "DUE", "COMP?", "REM?", "MOD?"))
        for subtask in subtasks:
            print("%-10s %-20s %-10s %-10s %-10s %-10s" % (str(subtask.uid), subtask.name, "%d/%d/%d" % (subtask.due.year, subtask.due.month, subtask.due.day), subtask.completed, subtask.removable, subtask.modifiable))

    def get_next_operation(self) -> DecisionEnum:
        choice = input("Choose operation [%s]: " % "\\".join(
            [enum.name for enum in DecisionEnum])).upper()
        return DecisionEnum[choice]

    def select_subtask(self) -> Subtask:
        subtask_id = int(
                input("SUBTASK ID:"))
        result = [
            subtask for subtask in self.displayed_subtasks if subtask_id == subtask.uid]
        if len(result) > 0:
            return result[0]

    def view_completion_rate(self):
        completed = 0
        for subtask in self.displayed_subtasks:
            if subtask.completed:
                completed += 1
        total = len(self.displayed_subtasks)
        result = completed / total * 100
        print("Completion rate: %f" % result)
