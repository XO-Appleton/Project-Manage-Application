class IssueEditingScreen:
    def display_form():
        iid = input("Enter issue number of the issue that you wish to edit: ")
        name = input("Enter the new issue title: ")
        description = input("Eneter the new issue description: ")
        return (iid, name, description)