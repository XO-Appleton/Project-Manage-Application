#This module is named budget but most of the function actually builds on the concept of fund management in a project setting.
#The best intuition I can come up with is like buying something. The budget plan tracks how much money you are probably gonna spend (starting from 0 cash),
#fund request is the process of taking cash from a ATM which requires a verifying process and the expense report serves as a recipt (Tracks what you spent on
# and also takes cash from you)

class BudgetPlan:
    #Budget Plan Object

    num_plan_created = 0 

    def __init__(self, project_id, plan_id = -1, Title = '', Description = '', expect_budget = 0, available_fund = 0):

        #The Budget Plan_id (same with Fund Request and Expense report) are the number of total BP/FR/ER that had been added
        #plan_id of -1 means it's a new plan
        if plan_id == -1:
            BudgetPlan.num_plan_created += 1
            self.plan_id = BudgetPlan.num_plan_created
        else:
            self.plan_id = plan_id
        self.project_id = project_id
        self.Title = Title
        self.Description = Description
        self.expect_budget = expect_budget
        self.avaliable_fund = available_fund
        
        self.reports = []
        self.requests = []
    
    def add_report(self,report):
        #adding an expense report under a budget plan
        #An expense report represents a spense happened, so upon recording the available fund reduces by the cost.

        if self.avaliable_fund < report.cost:
            print('Sorry the cost is too high')
            return
        report.plan_id = self.plan_id
        self.reports.append(report)
        self.avaliable_fund -= report.cost
        print('Successfully added report!')
        return

    def add_request(self,request):
        #adding a fund request under a budget plan
        request.plan_id = self.plan_id
        self.requests.append(request)
        print('Request added, waiting to be reviewed!')
        return

    def delete_report(self, rpt_id):
        #deleting an expense report from a budget plan
        for report in self.reports:
            if report.report_id == rpt_id:
               self.reports.remove(report)
               self.avaliable_fund += report.cost
               print('Report has been removed!')

    def delete_request(self, rqt_id):
        #deleting a fund request from a budget plan
        for request in self.requests:
            if request.request_id == rqt_id:
               self.requests.remove(request)
               print('Request has been removed!')

    def review(self, request_id, is_admin):
        #reviewing a fund request (only admin)
        #upon approval, the requested amount will be added to the available fund of the budget plan
        if is_admin == False:
            print("Only admin can review a Fund Request.")
            return
        
        for rqt in self.requests:
            if rqt.request_id == request_id:
                decision = input('Do you want to approve the request?(y/n)')
                if decision == 'y':
                    rqt.approval = True
                    self.avaliable_fund += rqt.amount
                    print('Request approved!')
                    return
                print('Request has been denied')
                return
        print('Request id {} does not match any request in the database'.format(request_id))
        return

    def to_dict(self):
        #Convert the Objects to dict type for json processing
        info = {
            'project_id': str(self.project_id),
            'plan_id': str(self.plan_id),
            'title': self.Title,
            'description': self.Description,
            'budget': str(self.expect_budget),
            'fund': str(self.avaliable_fund)
        }
        return info

    @classmethod
    def from_dict(cls, info):
        #Built from a dict, same with ExpenseReport and FundRequest's from_dict
        return cls(int(info['project_id']), int(info['plan_id']), info['title'], info['description'], int(info['budget']), int(info['fund']))
        

class ExpenseReport:
    #Expense Report Object
    
    num_report_created = 0

    def __init__(self, plan_id, report_id = -1, Title = '', Description = '', cost = 0):
        if report_id == -1:
            ExpenseReport.num_report_created += 1
            self.report_id = ExpenseReport.num_report_created
        else:
            self.report_id = report_id
        self.plan_id = plan_id
        self.Title = Title
        self.Description = Description
        self.cost = cost

    def to_dict(self):
        info = {
            'plan_id': str(self.plan_id),
            'report_id': str(self.report_id),
            'title': self.Title,
            'description': self.Description,
            'cost': str(self.cost)
        }
        return info

    @classmethod
    def from_dict(cls, info):
        return cls(int(info['plan_id']), int(info['report_id']), info['title'], info['description'], int(info['cost']))


class FundRequest:
    #Fund Request Object

    num_request_created = 0

    def __init__(self, plan_id, request_id = -1, Title = '', Description = '', amount = 0, approval = False):
        if request_id == -1:
            FundRequest.num_request_created += 1
            self.request_id = FundRequest.num_request_created
        else:
            self.request_id = request_id
        self.plan_id = plan_id
        self.Title = Title
        self.Description = Description
        self.amount = amount
        self.approval = approval

    def to_dict(self):
        info = {
            'plan_id': str(self.plan_id),
            'request_id': str(self.request_id),
            'title': self.Title,
            'description': self.Description,
            'amount': str(self.amount),
            'approval': str(self.approval)
        }
        return info

    @classmethod
    def from_dict(cls, info):
        return cls(int(info['plan_id']), int(info['request_id']), info['title'], info['description'], info['amount'], bool(info['approval']))
