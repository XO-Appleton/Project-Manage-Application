class Contact:
    def __init__(self, contact_id, first_name, last_name, details, private_details):
        self.contact_id = int(contact_id)
        self.first_name = first_name
        self.last_name = last_name
        self.details = details
        self.private_details = private_details
        self.contact_dict = {
            'id': contact_id,
            'first_name': first_name,
            'last_name': last_name,
            'details': details,
            'private_details': private_details
        }