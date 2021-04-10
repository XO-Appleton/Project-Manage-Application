from user import User
from project import Project
from feature_selection_screen import FeatureSelectionScreen

class FeatureSelector:
    
    def __init__(self):
        self.avail_proxy = []
        try:
            from progression_tracking_proxy import ProgressionTrackingProxy
            self.avail_proxy.append(ProgressionTrackingProxy())
        except ImportError:
            pass
        try:
            from contact_book_proxy import ContactBookProxy
            self.avail_proxy.append(ContactBookProxy())
        except ImportError:
            pass
        try:
            from budgeting_proxy import BudgetingProxy
            self.avail_proxy.append(BudgetingProxy())
        except ImportError:
            pass
        try:
            from announcement_proxy import AnnouncementProxy
            self.avail_proxy.append(AnnouncementProxy())
        except ImportError:
            pass
        try:
            from issue_tracking_proxy import IssueTrackingProxy
            self.avail_proxy.append(IssueTrackingProxyProxy())
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
