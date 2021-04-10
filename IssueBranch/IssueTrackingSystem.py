import sqlite3
from sqlite3 import Error

import sys
sys.path.append(".")

class Issue:
    def __init__(self, uid, iid, issue_name, issue_description, date):
        self.uid = uid
        self.iid = iid
        self.issue_name = issue_name
        self.issue_description = issue_description
        self.date = date

class IssueTrackingSystem:
    def sql_connect():
        try:
            conn = sqlite3.connect(r"C:\Users\dbedn\se3a04_2020_2021_t2_g5\IssueBranch\test.db")
            return conn
        except Error:
            print(Error)

    def create_table(conn, pid):
        cursor = conn.cursor()
        command = "CREATE TABLE issueDB"+ str(pid) +"(uid integer, iid integer PRIMARY KEY, issue_name text, issue_description text, date text)"
        cursor.execute(command)
        conn.commit()

    def add_issue(conn, issue, pid):
        open_issue = (issue.uid, issue.iid, issue.issue_name, issue.issue_description, issue.date)
        cursor = conn.cursor()
        command = 'INSERT INTO issueDB'+ str(pid) +'(uid, iid, issue_name, issue_description, date) VALUES(?, ?, ?, ?, ?)'
        cursor.execute(command, open_issue)
        conn.commit()
        return

    def edit_issue(conn, issue, pid):
        cursor = conn.cursor()
        com1 = 'UPDATE issueDB'+ str(pid) +' SET issue_name ="'+issue.issue_name
        com2 = '", issue_description ="'+issue.issue_description
        com3 = '", date ="'+str(issue.date)
        com4 = '" WHERE iid ='+issue.iid
        command = com1+com2+com3+com4

        cursor.execute(command)
        conn.commit()
        return
        
    def delete_issue(conn, iid, pid):
        cursor = conn.cursor()
        command = "DELETE FROM issueDB"+ str(pid) +" WHERE iid="+iid

        cursor.execute(command)
        conn.commit()
        return

    def num_issues(conn, pid):
        issue_list = IssueTrackingSystem.get_data(conn, pid)
        if issue_list == []:
            return 0
        return int(issue_list[-1].iid)

    def get_data(conn, pid):
        cursor = conn.cursor()

        command = "SELECT count(name) FROM sqlite_master WHERE type='table' AND name='issueDB"+str(pid)+"'"
        cursor.execute(command)
        file_exist = cursor.fetchall()
        if file_exist[0][0] == 0:
            IssueTrackingSystem.create_table(conn, pid)

        cursor.execute('SELECT * FROM issueDB'+ str(pid) )
        rows = cursor.fetchall()
        
        issue_list = []
        for i in range(len(rows)):
            issue = Issue(rows[i][0], rows[i][1], rows[i][2], rows[i][3], rows[i][4])
            issue_list.append(issue)

        return issue_list