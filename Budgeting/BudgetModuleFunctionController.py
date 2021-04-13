from BudgetUtils import *
from BudgetScreens import *
from BudgetDataSystem import *

class BudgetModuleFunctionController:

    def __init__(self, project_id: int, user):
        self.project_id = project_id
        self.user = user

    def initialize(self, project_id):
        self.main_screen = BudgetPlanMainScreen(True)
        self.plan_view_screen = BudgetPlanViewScreen(True)
        self.plan_mod_screen = BudgetPlanModificationScreen(True)
        self.report_mod_screen = ExpenseReportModificationScreen(True)
        self.request_mod_screen = FundRequestModificationScreen(True)
        self.database = BudgetDataSystem()

        self.plans = self.database.find_project(project_id)

        #Keep asking user for the next operation
        try:
            self.main_screen.display(self.plans)
            while True:
                cmd = self.main_screen.capture_event()
                self.handle_event(cmd)

        #Handles 'back' command
        except AssertionError:
            self.terminate()

    def handle_event(self,cmd):
        try:
            if len(cmd) < 1:
                raise IndexError
            if len(cmd) == 1:
                operation = cmd[0]
            if len(cmd) == 2:
                operation = cmd[0]
                file_type = cmd[1]
            if len(cmd) == 3:
                operation = cmd[0]
                file_type = cmd[1]
                opt_id = int(cmd[2])

            #User choose to view a budget obj
            if operation == 'VIEW':
                if file_type == 'PLAN':
                    plan = self.find_plan(opt_id)
                    self.plan_view_screen.display_plan(plan)
                elif file_type == 'REPORT':
                    report = self.find_report(opt_id)[1]
                    self.plan_view_screen.display_report(report)
                    return
                elif file_type == 'REQUEST':
                    request = self.find_request(opt_id)[1]
                    self.plan_view_screen.display_request(request)
                    return
                elif file_type == 'ALL':
                    self.main_screen.display(self.plans)
                else:
                    print('format: view plan/report/request id OR view all')
                    return
            
            #User choose to create a budget obj
            elif operation == 'CREATE':
                if file_type == 'PLAN':
                    crt_plan = self.plan_mod_screen.capture_input()
                    self.database.add_plan(crt_plan)
                    self.plans = self.database.find_project(self.project_id)
                    return
                elif file_type == 'REPORT':
                    plan_id = self.plan_mod_screen.get_plan_id()
                    #Check if the plan exist before entering info
                    self.find_plan(plan_id)
                    report = self.report_mod_screen.capture_input(plan_id)
                    self.database.add_report(report)
                    self.plans = self.database.find_project(self.project_id)
                    return
                elif file_type == 'REQUEST':
                    plan_id = self.plan_mod_screen.get_plan_id()
                    #Check if the plan exist before entering info
                    self.find_plan(plan_id)
                    request = self.request_mod_screen.capture_input(plan_id)
                    self.database.add_request(request)
                    self.plans = self.database.find_project(self.project_id)
                    return
                else:
                    print('format: create plan/report/request')
                    return
                
            #User choose to delete a budget obj
            elif operation == 'DELETE':
                if file_type == 'PLAN':
                    self.plans.remove(self.find_plan(opt_id))
                    self.database.delete_plan(opt_id)
                    return
                elif file_type == 'REPORT':
                    plan, report = self.find_report(opt_id)
                    plan.delete_report(report)
                    self.database.delete_report(plan.plan_id, report.report_id)
                    return
                elif file_type == 'REQUEST':
                    plan, request = self.find_request(opt_id)
                    plan.delete_request(request)
                    self.database.delete_request(plan.plan_id, request.request_id)
                    return
                else:
                    print('format: delete plan/report/request id')
                    return

            #User choose to edit a budget obj
            elif operation == 'EDIT':
                if file_type == 'PLAN':
                    plan = self.find_plan(opt_id)
                    plan = self.plan_mod_screen.display(plan)
                    self.database.update_plan(plan)
                    self.plans = self.database.find_project(self.project_id)

                elif file_type == 'REPORT':
                    plan = self.find_report(opt_id)[0]
                    plan = self.report_mod_screen.display(plan, opt_id)
                    self.database.update_plan(plan)
                    self.plans = self.database.find_project(self.project_id)
                    return
                elif file_type == 'REQUEST':
                    plan = self.find_request(opt_id)[0]
                    plan = self.request_mod_screen.display(plan, opt_id)
                    self.database.update_plan(plan)
                    self.plans = self.database.find_project(self.project_id)
                    return
                else:
                    print('format: edit plan/report/request id')
                    return

            elif operation == 'REVIEW':
                if file_type == 'REQUEST':
                    plan = self.find_request(opt_id)[0]
                    plan = self.request_mod_screen.review(plan, opt_id)
                    return
                else:
                    print('format: review request id')
                    return

            elif operation == 'BACK':
                raise AssertionError

        except ValueError:
            #Handles situation where the budget file id entered by user is not found
            print('Id does not match an existing record')
            return
        except IndexError:
            print('Wrong number of input arguments')
            return
        except KeyboardInterrupt:
            print('Cancelled by the user')
            return
        except AssertionError:
            raise AssertionError
        except:
            print('Something went wrong, please check your command')
            return
                    
                
    def find_plan(self, plan_id) -> BudgetPlan:
        for plan in self.plans:
            if plan.plan_id == plan_id:
                return plan
        raise ValueError

    def find_report(self, report_id) -> ExpenseReport:
        for plan in self.plans:
            for report in plan.reports:
                if report.report_id == report_id:
                    return plan, report
        raise ValueError

    def find_request(self, request_id) -> FundRequest:
        for plan in self.plans:
            for request in plan.requests:
                if request.request_id == request_id:
                    return plan, request
        raise ValueError

    def update_plan(self, plan: BudgetPlan):
        self.database.update_plan(plan)
        return
           

    def terminate(self):
        self.plans = None
        self.user = None
        self.project_id = None
        self.database.save()
        return


#Test
if __name__=='__main__':
    # bp1 = BudgetPlan(1, 'first bp', 'this is the first bp.', 100)
    # ex1 = ExpenseReport(1, 'first ER under bp1', 'this is the first ER under BP 1', 80)
    # fr1 = FundRequest(1, 'Gif money ovo', 'gimme 100 bucks man', 100)
    # bp2 = BudgetPlan(1, 'second bp', 'this is the second bp :)', 40)

    # BudgetPlanViewScreen(True).display(bp1)
    # bp1.add_request(fr1)
    # BudgetPlanViewScreen(True).display(bp1)

    # FundRequestModificationScreen(True).review(bp1,1)
    # BudgetPlanViewScreen(True).display(bp1)

    # bp1.add_report(ex1)
    # BudgetPlanViewScreen(True).display(bp1)

    # BudgetPlanModificationScreen().display(bp1)
    # BudgetPlanViewScreen().display(bp1)

    # ctl = BudgetModuleFunctionController(1, 0)

# class a:
#     def __init__(self) -> None:
#         self.value = ['abcdefg', 'hijklmn']

# class b:
#     def __init__(self,obj):
#         self.obj = obj
#     def func(self, test: a):
#         for i in test.value:
#             if i == 'abcdefg':
#                 test.value.remove(i)
#         return

# a1 = a()
# b1 = b(a1)

# b1.func(a1)
# print(b1.obj.value)
    pass
