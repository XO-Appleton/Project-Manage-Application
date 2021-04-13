from BudgetUtils import *
import json

class BudgetDataSystem:
    
    plan_storage_file_path = "./budget_plan_storage.json"
    report_storage_file_path = "./budget_report_storage.json"
    request_storage_file_path = "./budget_request_storage.json"

    def __init__(self) -> None:
        #Get Budget plans, Expense Reports and Fund Requests from the storage files
        with open(self.plan_storage_file_path, "r") as f:
            self.plans = [BudgetPlan.from_dict(plan) for plan in json.load(f)]
        with open(self.report_storage_file_path, "r") as f:
            self.reports = [ExpenseReport.from_dict(report) for report in json.load(f)]
        with open(self.request_storage_file_path, "r") as f:
            self.requests = [FundRequest.from_dict(request) for request in json.load(f)]

        max_plan_id = 0
        max_report_id = 0
        max_request_id = 0

        #Reconstruct the file structure and also recover the id count from the last session
        for plan in self.plans:
            if plan.plan_id > max_plan_id:
                max_plan_id = plan.plan_id
            for report in self.reports:
                if report.report_id > max_report_id:
                    max_report_id = report.report_id
                if report.plan_id == plan.plan_id:
                    plan.reports.append(report)
            for request in self.requests:
                if request.request_id > max_request_id:
                    max_request_id = request.request_id
                if request.plan_id == plan.plan_id:
                    plan.requests.append(request)

        BudgetPlan.num_plan_created = max_plan_id
        ExpenseReport.num_report_created = max_report_id
        FundRequest.num_request_created = max_request_id

    def find_project(self, project_id):
        #Find all the budget plans under the identified project
        return [plan for plan in self.plans if plan.project_id == project_id]

    def delete_project(self, project_id):
        for plan in self.plans:
            if plan.project_id == project_id:
                self.delete_plan(plan)

    def find_plan(self, plan_id) -> BudgetPlan:
        for plan in self.plans:
            if plan.plan_id == plan_id:
                return plan
            
    def add_plan(self, plan: BudgetPlan):
        self.plans.append(plan)

    def update_plan(self, plan: BudgetPlan):
        #This is used to update any changes on plan/report/request as the latter two belongs to the budget plan
        self.plans.remove(self.find_plan(plan.plan_id))
        self.plans.append(plan)

    def delete_plan(self, plan_id):
        #Upon deleting a budget plan, all the reports and requests get deleted as well
        for report in self.find_plan(plan_id).reports:
            self.delete_report(plan_id, report.report_id)
        for request in self.find_plan(plan_id).requests:
            self.delete_request(plan_id, request.request_id)
        self.plans.remove(self.find_plan(plan_id))

    def add_report(self, report: ExpenseReport):
        self.find_plan(report.plan_id).add_report(report)
        self.reports.append(report)

    def add_request(self,request: FundRequest):
        self.find_plan(request.plan_id).add_request(request)
        self.requests.append(request)

    def delete_report(self, plan_id, report_id):
        self.find_plan(plan_id).delete_report(report_id)
        for report in self.reports:
            if report.report_id == report_id:
                self.reports.remove(report)

    def delete_request(self, plan_id, request_id):
        self.find_plan(plan_id).delete_request(request_id)
        for request in self.requests:
            if request.request_id == request_id:
                self.requests.remove(request)

    def save(self):
        #Save Budget plans, Expense Reports and Fund Requests to the storage files
        self.plans = [plan.to_dict() for plan in self.plans]
        self.reports = [report.to_dict() for report in self.reports]
        self.requests = [request.to_dict() for request in self.requests]

        with open(self.plan_storage_file_path, "w") as f:
            json.dump(self.plans, f)
        with open(self.report_storage_file_path, "w") as f:
            json.dump(self.reports, f)
        with open(self.request_storage_file_path, "w") as f:
            json.dump(self.requests, f)

    