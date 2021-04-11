from Project import Project
from datetime import date
from User import User

class ProjectCreationScreen:

    def display_form(self, user: User) -> Project:
        project = Project()
        project.name = input("PROJECT NAME:")
        project.date_created = date.today()
        due_year = int(input("YEAR DUE:"))
        due_month = int(input("MONTH DUE:"))
        due_day = int(input("DAY DUE:"))
        project.due_date = date(due_year, due_month, due_day)
        project.admin = user
        project.member = []
        project.completed = False
        project.description = input("PROJECT DESCRIPTION:")
        return project


if __name__ == "__main__":
    print(ProjectCreationScreen().display_form(User()).description)