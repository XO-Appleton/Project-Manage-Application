import json
from Contact import Contact
import os

class ContactDatabase:
    
    def __init__(self):
        if not os.path.exists('contact_database.json'):
            with open('contact_database.json', 'w') as outfile:
                json.dump({}, outfile)


    def add_contact(self, project_id, contact):
        db = open("contact_database.json", "r")
        contact_full_list = json.load(db)
        db.close()
        
        if str(project_id) not in contact_full_list:
            contact_full_list[str(project_id)] = {}
        
        contact_full_list[str(project_id)][str(contact.contact_id)] = contact.contact_dict

        db = open("contact_database.json", "w+")
        db.write(json.dumps(contact_full_list, indent=4))
        db.close()

    def get_contacts(self, project_id):
        db = open("contact_database.json", "r")
        contacts = json.load(db)
        db.close()

        if str(project_id) in contacts:
            return contacts[str(project_id)]
        else:
            return None

    def get_contact(self, project_id, id):
        contacts = self.get_contacts(project_id)
        if contacts is not None:
            if str(id) in contacts:
                return contacts[str(id)]
            else:
                return None

    def delete_contact(self, project_id, id):
        db = open("contact_database.json", "r")
        contact_full_list = json.load(db)
        db.close()

        del contact_full_list[str(project_id)][str(id)]

        db = open("contact_database.json", "w+")
        db.write(json.dumps(contact_full_list, indent=4))
        db.close()

    def update_contact(self, project_id, updated):
        db = open("contact_database.json", "r")
        contact_full_list = json.load(db)
        db.close()

        contact_full_list[str(project_id)][str(updated.contact_id)] = updated.contact_dict

        db = open("contact_database.json", "w+")
        db.write(json.dumps(contact_full_list, indent=4))
        db.close()

if __name__ == "__main__":
    test = ContactDatabase()