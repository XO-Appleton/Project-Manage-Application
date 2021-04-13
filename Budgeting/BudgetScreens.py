from BudgetUtils import *
from BudgetModuleFunctionController import *

class Screen:

    def __init__(self,project_id, is_admin = True):
        self.is_admin = is_admin
        self.project_id = project_id

    def capture_event(self):
        #Available operations and file types
        cmd_op = ['VIEW', 'CREATE', 'DELETE', 'EDIT', 'REVIEW', 'BACK']
        file_op = ['PLAN', 'REPORT', 'REQUEST', 'ALL']

        try:
            #Record the user command and send it to caller
            while True:
                print('Please enter a command: ')
                cmd = input('Format: view/create/delete/edit/review/back (plan/report/request/all fileID)[optional]').upper().split(' ')
                return cmd

        except:
            return
            

    def print_BP(self, plan:BudgetPlan): 
        #Print a single Budget Plan
        print('------------------------------------------------------------------------')
        print('Budget Plan ID: ', str(plan.plan_id), '\n')
        print('Project ID: ', str(plan.project_id), '\n')
        print('Title: \n', plan.Title, '\n')
        print('Description: \n', plan.Description, '\n')
        print('Budget: ', str(plan.expect_budget), '\n')
        print('Available Fund: ', str(plan.avaliable_fund), '\n')
        print('------------------------------------------------------------------------')

    def print_ER(self, report:ExpenseReport):
        #Print a single Expense Report
        print('------------------------------------------------------------------------')
        print('Report ID: ', str(report.report_id), '\n')
        print('Plan ID: ', str(report.plan_id), '\n')
        print('Title: ', report.Title, '\n')
        print('Description: \n', report.Description, '\n')
        print('Cost: ', str(report.cost), '\n')
        print('------------------------------------------------------------------------')

    def print_FR(self, request:FundRequest):
        #Print a single Fund Request
        print('------------------------------------------------------------------------')
        print('Request ID: ', str(request.request_id), '\n')
        print('Plan ID: ', str(request.plan_id), '\n')
        print('Title: \n', request.Title, '\n')
        print('Description: \n', request.Description, '\n')
        print('amount: ', str(request.amount), '\n')
        print('Approval: ', request.approval)
        print('------------------------------------------------------------------------')

class BudgetPlanMainScreen(Screen):

    def __init__(self, project_id, is_admin=False):
        super().__init__(project_id, is_admin)

    def display(self, plan_list: list):
        try:
            #List all the Budget Plans under a project
            print('------------------------------------------------------------------------')
            print('All plans under the project ', str(plan_list[0].project_id), ':')
            for plan in plan_list:
                print('id: ', plan.plan_id, plan.Title)
            print('------------------------------------------------------------------------')
            return
        except IndexError:
            print('There is currently no Budget Plans under the project') 
            return
        

class BudgetPlanViewScreen(Screen):
    def __init__(self, project_id, is_admin=False):
        super().__init__(project_id, is_admin)

    def display_plan(self, plan: BudgetPlan):
        #View a Budget Plan's info along with all the Expense Reports and Fund Requests under it
        self.print_BP(plan)
        print('Expense Reports under the plan:\n')
        for report in plan.reports:
            self.print_ER(report)
        print('Fund requests under the plan:\n')
        for request in plan.requests:
            self.print_FR(request)
        return

    def display_report(self, report: ExpenseReport):
        self.print_ER(report)
        return

    def display_request(self, request: FundRequest):
        self.print_FR(request)
        return
    

class BudgetPlanModificationScreen(Screen):

    def __init__(self, project_id, is_admin=False):
        super().__init__(project_id, is_admin)

    def display(self, plan: BudgetPlan):
        #Displays the modifying Budget Plan then do the editing Process
        print('Current Plan:')
        self.print_BP(plan)
        try:
            dummy_plan = self.capture_input()
            dummy_plan.plan_id = plan.plan_id
            dummy_plan.avaliable_fund = plan.avaliable_fund
            dummy_plan.reports = plan.reports
            dummy_plan.requests = plan.requests

            #Confirm changes, if not return the original plan
            print('Preview of the report:')
            self.print_BP(dummy_plan)
            submit = input('Would you like to save the changes? (y/n)')
            if submit == 'y':
                plan = dummy_plan
            return plan
        except KeyboardInterrupt:
            raise KeyboardInterrupt
        except:
            print('Something went wrong. Please check your input!')
            return plan

    def capture_input(self) -> BudgetPlan:
        try:
            new_title = input('Enter the title: ')
            new_description = input('Enter the description: ')
            new_budget = int(input('Enter the expect budget: '))
            return BudgetPlan(int(self.project_id), Title = new_title, Description = new_description, expect_budget = new_budget)
        except KeyboardInterrupt:
            raise KeyboardInterrupt
        except:
            print('Something went wrong, Pls check ur input!')

    def get_plan_id(self):
        return int(input('Which plan do you want to add it on? '))
        

class ExpenseReportModificationScreen(Screen):

    def __init__(self, project_id, is_admin=False):
        super().__init__(project_id, is_admin)

    def display(self, plan: BudgetPlan, report_id):
        #Similar to the Budget Plan
        #Upon submit the modified report will be saved in the Budget Plan it's in
        try:
            for rpt in plan.reports:
                if rpt.report_id == report_id:
                    print('Current Report:')
                    self.print_ER(rpt)
                    dummy_report = self.capture_input(plan.plan_id)
                    dummy_report.report_id = rpt.report_id
                    print('Preview of the report:')
                    self.print_ER(dummy_report)
                    submit = input('Would you like to save the changes? (y/n)')
                    if submit == 'y':
                        rpt = dummy_report
                    return plan
            print('Sorry, there is no Expense Report matching the id.')
            return plan
        except KeyboardInterrupt:
            raise KeyboardInterrupt
        except:
            print('Something went wrong. Pls check your input!')
            
        
    def capture_input(self, plan_id):
        try:    
            new_title = input('Enter the title: ')
            new_description = input('Enter the description: ')
            new_cost = int(input('Enter the cost: '))
            return ExpenseReport(plan_id, Title = new_title, Description = new_description, cost = new_cost)
        except KeyboardInterrupt:
            raise KeyboardInterrupt
        except:
            print('Something went wrong. Pls check ur input!')


class FundRequestModificationScreen(Screen):

    def __init__(self, project_id, is_admin=True):
        super().__init__(project_id, is_admin)

    def display(self, plan: BudgetPlan, request_id):
        #Similar to the expense report editing
        try:    
            for rqt in plan.requests:
                if rqt.request_id == request_id:
                    print('Current Request:')
                    self.print_FR(rqt)
                    dummy_request = self.capture_input(plan.plan_id)
                    dummy_request.request_id = rqt.request_id
                    print('Preview of the request:')
                    self.print_FR(dummy_request)
                    submit = input('Would you like to save the changes? (y/n)')
                    if submit == 'y':
                        rqt = dummy_request
                    return plan
                print('Sorry, there is no Fund Request matching the id.')
                return plan
        except KeyboardInterrupt:
            raise KeyboardInterrupt
        except:
            print('Something went wrong. Pls check your input!')
        
    def capture_input(self, plan_id):
        try:
            new_title = input('Enter the title: ')
            new_description = input('Enter the description: ')
            new_amount = int(input('Enter the amount: '))
            return FundRequest(plan_id, Title = new_title, Description = new_description, amount = new_amount)
        except KeyboardInterrupt:
            raise KeyboardInterrupt
        except:
            print('Something went wrong. Pls check ur input!')

    def review(self, plan: BudgetPlan, request_id):
        #The admin can review a fund request and approve it or deny it
        plan.review(request_id, self.is_admin)



