import json
from datetime import date
from os.path import *

from User import User
from Project import Project
from CredentialDatabase import CredentialDatabase

class ProjectDataBase:

    __json_dump_file_name = "core_project_db.json"
    project_records: list = None
    project_count = None

    __instance = None

    def __init__(self):
        self.load_database()

    def add_project(self, project: Project):
        project.uid = self.project_count
        self.project_count += 1
        self.project_records.append(project)
        self.save_database()

    def change_project(self, project_id: int, project: Project):
        for i in range(len(self.project_records)):
            if self.project_records[i].get_uid() == project_id:
                self.project_records.pop(i)
                self.project_records.append(project)
                break
        self.save_database()

    def delete_project(self, project_id: int):
        for i in range(len(self.project_records)):
            if self.project_records[i].get_uid() == project_id:
                self.project_records.pop(i)
                break
        self.save_database()

    def get_project(self, project_id: int):
        for i in range(len(self.project_records)):
            if self.project_records[i].get_uid() == project_id:
                return self.project_records[i]

    def get_user_projects(self, user: User) -> list:
        return [p for p in self.project_records if user.get_user_ID() in [u.get_user_ID() for u in p.member] or user.get_user_ID() == p.admin.get_user_ID()]

    def load_database(self):
        self.project_records = []
        if not isfile(self.__json_dump_file_name):
            with open(self.__json_dump_file_name, "w") as fp:
                json.dump({"projects_count": 0, "json_records": []}, fp)
        
        with open(self.__json_dump_file_name) as fp:
            raw_str = fp.read()
            raw = json.loads(raw_str)
        self.project_count = raw["projects_count"]
        json_records = raw["json_records"]
        for d in json_records:
            p = Project()
            p.uid = d["uid"]
            p.name = d["name"]
            p.date_created = date(d["c_year"],d["c_month"],d["c_day"])
            p.due_date = date(d["d_year"],d["d_month"],d["d_day"])
            cdb = CredentialDatabase.get_instance()
            p.member = [cdb.get_user_from_id(each_id) for each_id in d["member"]]
            p.admin.user_ID = cdb.get_user_from_id(d["admin"])
            p.completed = d["completed"]
            p.description = d["description"]
            self.project_records.append(p)

    def save_database(self):
        json_records = []
        for p in self.project_records:
            d = {}
            d["uid"] = p.uid
            d["name"] = p.name
            d["c_year"] = p.date_created.year
            d["c_month"] = p.date_created.month
            d["c_day"] = p.date_created.day
            d["d_year"] = p.due_date.year
            d["d_month"] = p.due_date.month
            d["d_day"] = p.due_date.day
            d["member"] = [u.user_ID for u in p.member]
            d["admin"] = p.admin.user_ID
            d["completed"] = p.completed
            d["description"] = p.description
            json_records.append(d)
        with open(self.__json_dump_file_name, "w") as fp:
            json.dump({"projects_count": self.project_count, "json_records":json_records}, fp)

    @staticmethod
    def get_instance():
        if ProjectDataBase.__instance == None:
            ProjectDataBase.__instance = ProjectDataBase()
        return ProjectDataBase.__instance

    @staticmethod
    def get_dump_file_name():
        return ProjectDataBase.__json_dump_file_name


if __name__ == "__main__":
    import os
    os.remove(ProjectDataBase.get_dump_file_name())
    pdb = ProjectDataBase.get_instance()
    cdb = CredentialDatabase.get_instance()
    u1 = User()
    u1.first_name = "Lennon"
    u1.last_name = "Yu"
    u1.login_name = "yun12"
    cdb.add_user(u1)
    u2 = User()
    u2.first_name = "Dennis"
    u2.last_name = "Liao"
    u2.login_name = "liaod"
    cdb.add_user(u2)
    cdb.save_database()

    p = Project()
    p.name = "Project 1"
    p.description = "This is project 1"
    p.admin = u1
    p.member = [u2]
    p.date_created = date.today()
    p.due_date = date.today()
    p.completed = False
    pdb.add_project(p)
    pdb.save_database()