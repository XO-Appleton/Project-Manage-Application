from AnnouncementMasterController import AnnouncementMasterController
from User import User

# Starts the announcement branch.
# Also communicates with the core branch to deliver the current project and user
# to the announcement branch.


class AnnouncementProxy:
    def __init__(self):
        self.branch_name = "Announcement"

    # Returns the name of the branch
    def get_branch_name(self):
        return self.branch_name

    # Starts the branch using the main method in the Master Controller
    def start_branch(self, project_id, user):
        AnnouncementMasterController(project_id, user).main()


if __name__ == "__main__":
    testUser = User("Benjamin_Moore")
    test = AnnouncementProxy()
    test.start_branch(2, testUser)
