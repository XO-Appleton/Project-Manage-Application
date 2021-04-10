class ViewContactDetailsScreen:

    def __init__(self, viewing_contact):
        self.viewing_contact = viewing_contact

    def display_user(self):  
        print("\nViewing Contact")      
        print("****************************")
        print("ID: ", self.viewing_contact['id'])
        print("Name: ", self.viewing_contact['first_name'], self.viewing_contact['last_name'])
        print("Details: ", self.viewing_contact['details'])
        print("****************************")

    def display_admin(self):
        print("\nViewing Contact")  
        print("****************************")
        print("ID: ", self.viewing_contact['id'])
        print("Name: ", self.viewing_contact['first_name'], self.viewing_contact['last_name'])
        print("Details: ", self.viewing_contact['details'])
        print("Private details: ", self.viewing_contact['private_details'])
        print("****************************")

    def get_decision(self):
        print("Type 'delete', 'update', or 'exit'.")
        decision = input()
        return decision
