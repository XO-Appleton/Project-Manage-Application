from BudgetModuleFunctionController import *

# Starts the budgeting branch.
# Also communicates with the core branch to deliver the current project and user
# to the budgeting branch.


class BudgetingProxy:
    def __init__(self):
        self.branch_name = "Budgeting"

    # Returns the name of the branch
    def get_branch_name(self):
        return self.branch_name

    # Starts the branch using the main method in the Master Controller
    def start_branch(self, project_id, user):
        BudgetModuleFunctionController(project_id, user).initialize(project_id)
