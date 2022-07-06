class IssueListScreen:
    def display_List(issue_list, reply_list):

        print('')
        print('Issue List')
        print('')

        for issue in issue_list:
            issue_replies = []
            for reply in reply_list:
                if reply.iid == issue.iid:
                    issue_replies.append(reply.reply)

            print("Issue ", issue.iid, ":", issue.issue_name)
            print("description:", issue.issue_description)
            print("made by :", issue.uid, "on:", issue.date)
            print('Replies:')
            for r in issue_replies:
                print(r)
            print('')
            print('')

        print("The commands are as follows:")
        print("open, edit, close, and reply")
        command = input("Enter a command: ")

        return command
    
    def get_reply():
        return input("Enter your reply: ")