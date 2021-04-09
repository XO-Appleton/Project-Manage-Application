from announcementMasterController import AnnouncementMasterController
from User import User


class AnnouncementProxy:
    def __init__(self):
        self.branch_name = "Announcement"

    def get_branch_name(self):
        return self.branch_name

    def start_branch(self, project_id, user):
        AnnouncementMasterController(project_id, user).main()


# testUser = User("waterbottle")

# test = AnnouncementProxy()
# test.start_branch(5, testUser)
