from ContactBookController import ContactBookController
from User import User
from Project import Project

class ContactBookProxy:
    
    def __init__(self):
        self.branch_name = "Contact Book"

    def get_branch_name(self):
        return self.branch_name
    
    def start_branch(self, project, user):

        proj_admin = project.get_admin()
        if proj_admin.get_user_ID() == user.get_user_ID():
            print("Running as admin")
            ContactBookController(project.get_uid(), 'admin').main()
        else:
            print("Running as user")
            ContactBookController(project.get_uid(), 'user').main()