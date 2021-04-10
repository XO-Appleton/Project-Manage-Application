class BudgetPlan:
    #Budget Plan Object

    num_plan_created = 0 

    def __init__(self, project_id, Title, Description, expect_budget):
        self.project_id = project_id
        self.Title = Title
        self.Description = Description
        self.expect_budget = expect_budget
    
        #The Budget Plan_id (same with Fund Request and Expense report) are the number of total BP/FR/ER that had been added
        BudgetPlan.num_plan_created += 1
        self.plan_id = BudgetPlan.num_plan_created

        self.avaliable_fund = 0
        self.reports = []
        self.requests = []
    
    #adding an expense report under a budget plan
    def add_report(self,report):
        if self.avaliable_fund < report.cost:
            print('Sorry the cost is too high')
            return
        self.reports.append(report)
        self.avaliable_fund -= report.cost
        print('Successfully added report!')
        return

    #adding a fund request under a budget plan
    def add_request(self,request):
        self.requests.append(request)
        print('Request added, waiting to be reviewed!')
        return

    #deleting an expense report from a budget plan
    def delete_report(self, rpt_id):
        for report in self.reports:
            if report.report_id == rpt_id:
               self.reports.remove(report)
               print('Report has been removed!')

    #deleting a fund request from a budget plan
    def delete_request(self, rqt_id):
        for request in self.requests:
            if request.request_id == rqt_id:
               self.reports.remove(request)
               print('Request has been removed!')

    #reviewing a fund request (only admin)
    #upon approval, the requested amount will be added to the available fund of the budget plan
    def review(self, request, user):
        if user.is_admin() == False:
            print("Only admin can review a request.")
            return
        
        decision = input('Do you want to approve the request?(y/n)')
        if decision == 'y':
            request.proval = True
            avaliable_fund += request.cost
            print('Request approved!')
        return
        

class ExpenseReport:
    #Expense Report Object
    
    num_report_created = 0

    def __init__(self, plan_id, Title, Description, cost):
        self.plan_id = plan_id
        self.Title = Title
        self.Description = Description
        self.cost = cost
        ExpenseReport.num_report_created += 1
        self.report_id = ExpenseReport.num_report_created


class FundRequest:
    #Fund Request Object

    num_request_created = 0

    def __init__(self, plan_id, Title, Description, cost):
        self.plan_id = plan_id
        self.Title = Title
        self.Description = Description
        self.cost = cost
        FundRequest.num_request_created += 1
        self.request_id = FundRequest.num_request_created
        self.proval = False

#Test
if __name__=='__main__':
    bp1 = BudgetPlan(1, 'first bp', 'this is the first bp.', 100)
    
    ex1 = ExpenseReport(1, 'first ER under bp1', 'this is the first ER under BP 1', 80)
    fr1 = FundRequest(1, 'Gif money ovo', 'gimme 100 bucks man', 100)
    bp1.avaliable_fund += 100

    bp1.add_report(ex1)
    bp1.add_request(fr1)
    print(bp1.reports[0].report_id)

    bp2 = BudgetPlan(1, 'second bp', 'this is the second bp :)', 40)
    print(bp2.reports)

    bp1.delete_report(1)
    print(bp1.reports)