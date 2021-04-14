from datetime import date

from Subtask import Subtask

class SubtaskModificationScreen:

    def display_form(self, subtask: Subtask):
        print("Modifying subtask %s" % subtask.name)
        self.old_subtask = subtask

    def get_input(self, show_admin_fields = True) -> Subtask:
        name = input("NAME:")
        due_date = date(*[int(token) for token in input("DUE DATE [yyyy mm dd]:").split()])
        modifiable = self.old_subtask.modifiable
        removable = self.old_subtask.removable
        if show_admin_fields:
            modifiable = input("MODIFIABLE [T/F]:").upper() == "T"
            removable = input("REMOVABLE [T/F]:").upper() == "T"
        completed = self.old_subtask.completed
        return Subtask(None, name, due_date, completed, modifiable, removable)