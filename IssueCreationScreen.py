class IssueCreationScreen:
    def display_form():
        name = input("Eneter the issue title: ")
        description = input("Enter the issue description: ")
        return (name, description)