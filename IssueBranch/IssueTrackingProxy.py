from IssueController import IssueController

# Starts the issue branch.
# Also communicates with the core branch to deliver the current project and user
# to the issue branch.


class IssueTrackingProxy:
    def __init__(self):
        self.branch_name = "Issue"

    def get_branch_name(self):
        return self.branch_name

    def start_branch(self, project_id, user_id):
        IssueController(project_id, user_id)


pid = 1
uid = 1
test = IssueTrackingProxy()
test.start_branch(pid, uid)
