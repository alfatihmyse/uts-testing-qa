# test_contacts.py
import unittest
from contacts import Contact, ContactManager

class TestContactManager(unittest.TestCase):
    def setUp(self):
        self.manager = ContactManager()
        self.contact1 = Contact("Alice", "alice@example.com")
        self.contact2 = Contact("Bob", "bob@example.com")

    def test_add_contact(self):
        self.manager.add_contact(self.contact1)
        self.assertEqual(self.manager.get_contact("alice@example.com"), self.contact1)

    def test_remove_contact(self):
        self.manager.add_contact(self.contact1)
        self.manager.remove_contact("alice@example.com")
        self.assertIsNone(self.manager.get_contact("alice@example.com"))

    def test_get_all_contacts(self):
        self.manager.add_contact(self.contact1)
        self.manager.add_contact(self.contact2)
        contacts = self.manager.get_all_contacts()
        self.assertIn(self.contact1, contacts)
        self.assertIn(self.contact2, contacts)

if __name__ == "__main__":
    unittest.main()