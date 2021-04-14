from datetime import date

class Subtask:

    def __init__(self, uid: int, name: str, due: date, completed: bool, modifiable: bool, removable: bool):
        self.uid = uid
        self.name = name
        self.due = due
        self.completed = completed
        self.modifiable = modifiable
        self.removable = removable

    def get_dict(self):
        d = {}
        d["uid"] = self.uid
        d["name"] = self.name
        d["due_year"] = self.due.year
        d["due_month"] = self.due.month
        d["due_day"] = self.due.day
        d["completed"] = self.completed
        d["modifiable"] = self.modifiable
        d["removable"] = self.removable
        return d

    def copy(self):
        return Subtask(self.uid, "%s" % self.name, date(self.due.year, self.due.month, self.due.day), self.completed, self.modifiable, self.removable)

    @staticmethod
    def reconstruct(record: dict):
        s = Subtask(
                record["uid"],
                record["name"],
                date(record["due_year"], record["due_month"], record["due_day"]),
                record["completed"],
                record["modifiable"],
                record["removable"]
            )
        return s