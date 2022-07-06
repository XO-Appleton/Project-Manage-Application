from MainContactScreen import MainContactScreen
from CreateContactScreen import CreateContactScreen
from ContactDatabase import ContactDatabase
from Contact.UpdateContactScreen import UpdateContactScreen
from ViewContactDetailsScreen import ViewContactDetailsScreen

class ContactBookController:

    def __init__(self, project_id, user):
        self.project_id = project_id
        self.user = user

    def main(self):
        contact_list = ContactDatabase().get_contacts(self.project_id)
        main_screen = MainContactScreen(contact_list, self.user)

        while True:
            main_screen.display()
            decision = main_screen.get_request()

            if decision == 'view':
                viewing_contact_id = input("Enter contact ID to view: ")
                viewing_contact = ContactDatabase().get_contact(self.project_id, viewing_contact_id)
                self.view_contact(viewing_contact)
            elif decision == 'create' and self.user == 'admin':
                self.create_contact()
            elif decision == 'sort':
                sorted_list = self.sort_contact_list()
                main_screen = MainContactScreen(sorted_list, self.user)
            elif decision == 'search':
                search_name = input("Enter a first name to search for contacts: ")
                search_list = self.search_contact(search_name)
                search_screen = MainContactScreen(search_list, self.user)
                main_screen = MainContactScreen(search_list, self.user)
            elif decision == 'exit':
                return

            # refresh the contact list in case it gets updated
            if decision != 'sort' and decision != 'search':
                contact_list = ContactDatabase().get_contacts(self.project_id)
                main_screen = MainContactScreen(contact_list, self.user)

    def create_contact(self):
        CreateContactScreen().display_form()
        new = CreateContactScreen().get_input()
        ContactDatabase().add_contact(self.project_id, new)

    def update_contact(self, contact):
        UpdateContactScreen(contact).display_form()
        updated = UpdateContactScreen(contact).get_input()
        ContactDatabase().update_contact(self.project_id, updated)

    def view_contact(self, contact):
        view = ViewContactDetailsScreen(contact)

        if self.user == 'user': #not sure if User is determined by string 'user' or 'admin'
            view.display_user()
        elif self.user == 'admin':
            view.display_admin()

        decision = view.get_decision()

        if decision == 'delete' and self.user == 'admin':
            ContactDatabase().delete_contact(self.project_id, int(contact['id']))
        elif decision == 'update' and self.user == 'admin':
            self.update_contact(contact)
        elif decision == 'exit':
            return

    def sort_contact_list(self):
        result = {}
        contact_list = ContactDatabase().get_contacts(self.project_id)

        for i in range(65, 123): #check every letter char
            for c_id in contact_list:
                if ord(contact_list[c_id]['first_name'][0]) == i:
                    result[c_id] = contact_list[c_id]
        return result

    def search_contact(self, name):
        result = {}
        contact_list = ContactDatabase().get_contacts(self.project_id)

        for c_id in contact_list:
            if contact_list[c_id]['first_name'] == name:
                result[c_id] = contact_list[c_id]
        return result

#testing
if __name__ == "__main__":
    test = ContactBookController(1, 'admin')
    test.main()