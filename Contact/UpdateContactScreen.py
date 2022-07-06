import Contact

class UpdateContactScreen:
    def __init__(self, updating_contact):
        self.updating_contact = updating_contact

    def display_form(self):
        print("")
        print("Contact to be updated: ")
        print("****************************")
        print("Name: ", self.updating_contact['first_name'], self.updating_contact['last_name'])
        print("Details: ", self.updating_contact['details'])
        print("Private details: ", self.updating_contact['private_details'])
        print("****************************")

    def get_input(self):
        first_name = input("Enter the updated first name: ")
        last_name = input("Enter the updated last name: ")
        details = input("Enter the updated details: ")
        private_details = input("Enter the updated private details: ")
        return Contact(int(self.updating_contact['id']), first_name, last_name, details, private_details)
