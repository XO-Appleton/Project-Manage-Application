from User import User

class Project:

    def __init__(self):
        self.uid = None
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

    def is_admin(self, user: User) -> bool:
        return self.get_admin().get_user_ID() == user.get_user_ID()

    def __str__(self):
        return '''uid:\t%d
name:\t%s
date_created:\t%s
due_date:\t%s
member:\t%s
admin:\t%s
completed:\t%s
description:\t%s''' % (self.uid, self.name, self.date_created, \
            self.due_date, [m.get_login_name() for m in self.member], \
                self.admin.get_login_name(), self.completed, self.description)