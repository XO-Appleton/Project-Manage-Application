class ProgressionTrackingProxy:

    branch_name = "Progression Tracking"

    def __init__(self):
        pass

    def start_branch(self, project, user):
        print("Running feature branch:", self.branch_name)

    def get_branch_name(self):
        return self.branch_name