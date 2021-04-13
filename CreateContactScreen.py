from Contact import Contact

class CreateContactScreen:

    def display_form(self):
        print("")
        print("Create a Contact")
        print("****************************")

    def get_input(self):
        id = int(input("Enter contact ID: "))
        first_name = str(input("Enter the first name: "))
        last_name = str(input("Enter the last name: "))
        details = str(input("Enter the details: "))
        private_details = str(input("Enter the private details: "))

        return Contact(id, first_name, last_name, details, private_details)