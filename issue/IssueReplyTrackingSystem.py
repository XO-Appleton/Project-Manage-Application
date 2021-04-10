import sqlite3
from sqlite3 import Error

import sys
sys.path.append(".")

class Reply:
    def __init__(self, uid, iid, reply, rid):
        self.uid = uid
        self.iid = iid
        self.reply = reply
        self.rid = rid

class IssueReplyTrackingSystem:
    def sql_connect():
        try:
            conn = sqlite3.connect(r"C:\Users\dbedn\se3a04_2020_2021_t2_g5\IssueBranch\test.db")
            return conn
        except Error:
            print(Error)

    def create_table(conn, pid):
        cursor = conn.cursor()
        command = "CREATE TABLE replyDB"+ str(pid) +"(uid integer, iid integer, reply text, rid integer PRIMARY KEY)"
        cursor.execute(command)
        conn.commit()

    def add_reply(conn, new_reply, pid):
        reply = (new_reply.uid, new_reply.iid, new_reply.reply, new_reply.rid)
        cursor = conn.cursor()
        command = 'INSERT INTO replyDB'+ str(pid) +'(uid, iid, reply, rid) VALUES(?, ?, ?, ?)'
        cursor.execute(command, reply)
        conn.commit()
        return

    def num_replies(conn, pid):
        reply_list = IssueReplyTrackingSystem.get_data(conn, pid)
        if reply_list == []:
            return 0
        return int(reply_list[-1].rid)

    def get_data(conn, pid):
        cursor = conn.cursor()

        command = "SELECT count(name) FROM sqlite_master WHERE type='table' AND name='replyDB"+str(pid)+"'"
        cursor.execute(command)
        file_exist = cursor.fetchall()
        if file_exist[0][0] == 0:
            IssueReplyTrackingSystem.create_table(conn, pid)

        cursor.execute('SELECT * FROM replyDB'+ str(pid) )
        rows = cursor.fetchall()
        
        reply_list = []
        for i in range(len(rows)):
            reply = Reply(rows[i][0], rows[i][1], rows[i][2], rows[i][3])
            reply_list.append(reply)

        return reply_list

if __name__ == "__main__":
    conn = IssueReplyTrackingSystem.sql_connect()
    print(IssueReplyTrackingSystem.num_replies(conn, 1))