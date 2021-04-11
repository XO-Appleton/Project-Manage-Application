from User import User
from Project import Project
from FeatureSelectionScreen import FeatureSelectionScreen

class FeatureSelector:
    
    def __init__(self):
        self.avail_proxy = []
        try:
            from ProgressionTrackingProxy import ProgressionTrackingProxy
            self.avail_proxy.append(ProgressionTrackingProxy())
        except ImportError:
            pass
        try:
            from ContactBookProxy import ContactBookProxy
            self.avail_proxy.append(ContactBookProxy())
        except ImportError:
            pass
        try:
            from BudgetingProxy import BudgetingProxy
            self.avail_proxy.append(BudgetingProxy())
        except ImportError:
            pass
        try:
            from AnnouncementProxy import AnnouncementProxy
            self.avail_proxy.append(AnnouncementProxy())
        except ImportError:
            pass
        try:
            from IssueTrackingProxy import IssueTrackingProxy
            self.avail_proxy.append(IssueTrackingProxy())
        except ImportError:
            pass
        self.screen = FeatureSelectionScreen()

    def start_branch_usage(self, project, user):
        branch_names = [proxy.get_branch_name() for proxy in self.avail_proxy]
        self.screen.display_options(branch_names)
        branch_choice = self.screen.get_branch_choice()
        for proxy in self.avail_proxy:
            if branch_choice == proxy.get_branch_name():
                proxy.start_branch(project, user)
                return
        raise RuntimeError("Did not find the branch!")



if __name__ == "__main__":
    selector = FeatureSelector()
    selector.start_branch_usage(None, None)
