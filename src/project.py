from datetime import date

class Project:

    __global_uid = 0
    __uid = None
    name = None
    date_created = None
    due_date = None
    member = None
    __admin = None
    completed = None
    description = None

    def __init__(self):
        pass