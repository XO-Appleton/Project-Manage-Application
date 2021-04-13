class MainContactScreen:
    def __init__(self, contact_list, user):
        self.contact_list = contact_list
        self.user = user

    def display(self):
        print("\n****************************")
        print("Contact Book")
        print("****************************")
        if self.contact_list is None:
            return
        for c_id in self.contact_list:
            print("ID: ", self.contact_list[c_id]['id'])
            print("Name: ", self.contact_list[c_id]['first_name'], self.contact_list[c_id]['last_name'])
            print("Details: ", self.contact_list[c_id]['details'])
            if self.user == 'admin':
                print("Private Details: ", self.contact_list[c_id]['private_details'])
            print("------")
    
    def get_request(self):
        print("Type 'create', 'sort', 'view', 'search', or 'exit'.")
        decision = input()
        return decision