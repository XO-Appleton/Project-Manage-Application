class IssueListScreen:
    def display_List(issue_list):

        print('')
        print('Issue List')
        print('')

        for issue in issue_list:
            print("Issue ", issue.iid, ":", issue.issue_name)
            print("description:", issue.issue_description)
            print("made by :", issue.uid, "on:", issue.date)
            print('')

        print("The commands are as follows:")
        print("open, edit, close, and reply")
        command = input("Enter a command: ")

        return command