from ContactBookController import ContactBookController
from User import User
from Project import Project

class ContactBookProxy:
    
    def __init__(self):
        self.branch_name = "Contact Book"

    def get_branch_name(self):
        return self.branch_name
    
    def start_branch(self, project, user):
        #get project id from project, 
        #check if user is admin or user and pass it
        #ContactBookController(project_id, user).main()
        
        #for testing
        ContactBookController(1, 'admin').main()