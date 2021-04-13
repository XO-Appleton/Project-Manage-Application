from BudgetUtils import *
from BudgetScreens import *
from BudgetDataSystem import *
from BudgetingProxy import *

class BudgetModuleFunctionController:

    def __init__(self, project, user):
        self.project_id = project.get_uid()
        self.is_admin = user.get_user_ID() == project.get_admin().get_user_ID()
        self.user = user
        #Available operations and file types
        self.cmd_op = ['VIEW', 'CREATE', 'DELETE', 'EDIT', 'REVIEW', 'BACK']
        self.file_op = ['PLAN', 'REPORT', 'REQUEST', 'ALL']


    def initialize(self, project_id):
        self.main_screen = BudgetPlanMainScreen(self.is_admin)
        self.plan_view_screen = BudgetPlanViewScreen(self.is_admin)
        self.plan_mod_screen = BudgetPlanModificationScreen(self.is_admin)
        self.report_mod_screen = ExpenseReportModificationScreen(self.is_admin)
        self.request_mod_screen = FundRequestModificationScreen(self.is_admin)
        self.database = BudgetDataSystem()

        self.plans = self.database.find_project(project_id)

        #Keep asking user for the next operation
        try:
            self.main_screen.display(self.plans)
            while True:
                cmd = self.main_screen.capture_event()
                self.handle_event(cmd)

        #Handles 'back' command
        #Too lazy to actually make an
        # Exception class so I used AssertionError here :<
        except AssertionError:
            self.__terminate()

    def handle_event(self,cmd):
        try:
            if cmd[0] == '':
                raise IndexError
            elif cmd[0] not in self.cmd_op:
                raise TypeError
            elif cmd[1] not in self.file_op:
                raise SyntaxError
            else:
                operation, file_type, opt_id = cmd[0], cmd[1], int(cmd[2])
            
            #User choose to view a budget obj
            if operation == 'VIEW':
                if file_type == 'PLAN':
                    plan = self.__find_plan(opt_id)
                    self.plan_view_screen.display_plan(plan)
                elif file_type == 'REPORT':
                    report = self.__find_report(opt_id)[1]
                    self.plan_view_screen.display_report(report)
                     
                elif file_type == 'REQUEST':
                    request = self.__find_request(opt_id)[1]
                    self.plan_view_screen.display_request(request)
                     
                elif file_type == 'ALL':
                    self.main_screen.display(self.plans)
                else:
                    print('View Format: view plan/report/request id OR view all')
                     
            
            #User choose to create a budget obj
            elif operation == 'CREATE':
                if file_type == 'PLAN':
                    crt_plan = self.plan_mod_screen.capture_input()
                    self.database.add_plan(crt_plan)
                    self.plans = self.database.find_project(self.project_id)
                     
                elif file_type == 'REPORT':
                    plan_id = self.plan_mod_screen.get_plan_id()
                    #Check if the plan exist before entering info
                    self.__find_plan(plan_id)
                    report = self.report_mod_screen.capture_input(plan_id)
                    self.database.add_report(report)
                    self.plans = self.database.find_project(self.project_id)
                     
                elif file_type == 'REQUEST':
                    plan_id = self.plan_mod_screen.get_plan_id()
                    #Check if the plan exist before entering info
                    self.__find_plan(plan_id)
                    request = self.request_mod_screen.capture_input(plan_id)
                    self.database.add_request(request)
                    self.plans = self.database.find_project(self.project_id)
                     
                else:
                    print('Create Format: create plan/report/request')
                     
                
            #User choose to delete a budget obj
            elif operation == 'DELETE':
                if file_type == 'PLAN':
                    self.plans.remove(self.__find_plan(opt_id))
                    self.database.delete_plan(opt_id)
                    print('All the files under Plan {} has been deleted'.format(opt_id))
                     
                elif file_type == 'REPORT':
                    plan, report = self.__find_report(opt_id)
                    plan.delete_report(report)
                    self.database.delete_report(plan.plan_id, report.report_id)
                    print('Report {} has been deleted'.format(opt_id))
                     
                elif file_type == 'REQUEST':
                    plan, request = self.__find_request(opt_id)
                    plan.delete_request(request)
                    self.database.delete_request(plan.plan_id, request.request_id)
                    print('Request {} has been deleted'.format(opt_id))

                elif file_type == 'ALL':
                    self.database.delete_project(self.project_id)
                    print('All files under Project {} has been deleted'.format(self.project_id))
                     
                else:
                    print('Delete Format: delete plan/report/request/all id')
                     

            #User choose to edit a budget obj
            elif operation == 'EDIT':
                if file_type == 'PLAN':
                    plan = self.__find_plan(opt_id)
                    plan = self.plan_mod_screen.display(plan)
                    self.database.__update_plan(plan)
                    self.plans = self.database.find_project(self.project_id)

                elif file_type == 'REPORT':
                    plan = self.__find_report(opt_id)[0]
                    plan = self.report_mod_screen.display(plan, opt_id)
                    self.database.__update_plan(plan)
                    self.plans = self.database.find_project(self.project_id)
                     
                elif file_type == 'REQUEST':
                    plan = self.__find_request(opt_id)[0]
                    plan = self.request_mod_screen.display(plan, opt_id)
                    self.database.__update_plan(plan)
                    self.plans = self.database.find_project(self.project_id)
                     
                else:
                    print('Edit Format: edit plan/report/request id')
                     

            #User choose to review a fund request
            elif operation == 'REVIEW':
                if file_type == 'REQUEST':
                    plan = self.__find_request(opt_id)[0]
                    plan = self.request_mod_screen._review(plan, opt_id)
                     
                else:
                    print('Review Format: review request id')
                     

            #User exits the branch
            elif operation == 'BACK':
                raise AssertionError

        except TypeError:
            print('Invalid command')
        except SyntaxError:
            print('Invalid file type')
        except ValueError:
            #Handles situation where the budget file id entered by user is not found
            print('Id does not match an existing record')
        except IndexError:
            print('No input arguments detected')
        except KeyboardInterrupt:
            print('Cancelled by the user')
        except AssertionError:
            raise AssertionError
        # except:
        #     print('Something went wrong, please check your command')                    
                
    def __find_plan(self, plan_id) -> BudgetPlan:
        #Find a plan in the local list.
        #Not really serving any functions just making the code a little more compact.
        #Same with the other two below.
        for plan in self.plans:
            if plan.plan_id == plan_id:
                return plan
        raise ValueError

    def __find_report(self, report_id) -> ExpenseReport:
        for plan in self.plans:
            for report in plan.reports:
                if report.report_id == report_id:
                    return plan, report
        raise ValueError

    def __find_request(self, request_id) -> FundRequest:
        for plan in self.plans:
            for request in plan.requests:
                if request.request_id == request_id:
                    return plan, request
        raise ValueError

    def __update_plan(self, plan: BudgetPlan):
        #Any changes regarding to plan/report/request is encoded into a for-replace budget plan
        #and sent to the database.
        self.database.update_plan(plan)
           

    def __terminate(self):
        #Clear the cache (sorta) and return to core program.
        self.is_admin = False
        self.plans = None
        self.user = None
        self.project_id = None
        self.database.save()


#Test
if __name__=='__main__':
    
    pass
