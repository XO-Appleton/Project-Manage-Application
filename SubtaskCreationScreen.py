from datetime import date

from Subtask import Subtask

class SubtaskCreationScreen:

    def get_input(self, show_admin_field = True) -> Subtask:
        try:
            name = input("NAME:")
            due_date = date(*[int(token) for token in input("DUE DATE [yyyy mm dd]:").split()])
            modifiable = True
            removable = True
            if show_admin_field:
                modifiable = input("MODIFIABLE [T/F]:").upper() == "T"
                removable = input("REMOVABLE [T/F]:").upper() == "T"
        except TypeError:
            return self.get_input()
        return Subtask(None, name, due_date, False, modifiable, removable)