from datetime import date

class Project:

    __global_uid_count = 0

    def __init__(self):
        self.uid = self.__global_uid_count
        self.__global_uid_count += 1
        self.name = None
        self.date_created = None
        self.due_date = None
        self.member = None
        self.admin = None
        self.completed = None
        self.description = None

    def get_uid(self) -> int:
        return self.uid

    def get_admin(self) -> User:
        return self.admin