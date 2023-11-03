# contacts.py
class Contact:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def remove_contact(self, email):
        self.contacts = [c for c in self.contacts if c.email != email]

    def get_contact(self, email):
        for contact in self.contacts:
            if contact.email == email:
                return contact
        return None

    def get_all_contacts(self):
        return self.contacts