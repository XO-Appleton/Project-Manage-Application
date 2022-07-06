import datetime
import sqlite3
from sqlite3 import Error

import sys
sys.path.append(".")
from IssueTrackingSystem import Issue
from IssueReplyTrackingSystem import Reply
from IssueTrackingSystem import IssueTrackingSystem
from IssueListScreen import IssueListScreen
from IssueCreationScreen import IssueCreationScreen
from IssueEditingScreen import IssueEditingScreen
from IssueReplyTrackingSystem import IssueReplyTrackingSystem

class IssueController:
    def __init__(self, pid, user):
        self.uid = user.get_user_ID()
        self.pid = pid
        self.conn = IssueTrackingSystem.sql_connect()
        self.goto_list_screen()
    def goto_list_screen(self):
        while(True):
            issue_list = IssueTrackingSystem.get_data(self.conn, self.pid)
            reply_list = IssueReplyTrackingSystem.get_data(self.conn, self.pid)

            command = IssueListScreen.display_List(issue_list, reply_list)

            if(command == "open"):
                self.open()
                print('')
            elif(command == "edit"):
                self.edit()
                print('')
            elif(command == "close"):
                self.close()
                print('')
            elif(command == "reply"):
                self.reply()
                print('')
            else:
                print('')
                print('exiting')
                self.conn.close()
                return

    def open(self):
        issue_name, issue_description = IssueCreationScreen.display_form()
        iid = IssueTrackingSystem.num_issues(self.conn, self.pid) + 1
        date = datetime.date.today()

        issue = Issue(self.uid, iid, issue_name, issue_description, date)
        IssueTrackingSystem.add_issue(self.conn, issue, self.pid)
        return

    def edit(self):
        iid, issue_name, issue_description = IssueEditingScreen.display_form()
        date = datetime.date.today()

        issue = Issue(self.uid, iid, issue_name, issue_description, date)
        IssueTrackingSystem.edit_issue(self.conn, issue, self.pid)
        return
    
    def close(self):
        iid = input("Enter issue number of the issue that you wish to close: ")
        IssueTrackingSystem.delete_issue(self.conn, iid, self.pid)
        return

    def reply(self):
        iid = input("Enter issue number of the issue that you wish to reply to: ")
        rid = IssueReplyTrackingSystem.num_replies(self.conn, self.pid) + 1
        reply = IssueListScreen.get_reply()
        
        new_reply = Reply(self.uid, iid, reply, rid)
        IssueReplyTrackingSystem.add_reply(self.conn, new_reply, self.pid)
        return