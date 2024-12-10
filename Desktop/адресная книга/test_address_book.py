import unittest
from address_book import add_contact, delete_contact, edit_contact, load_contacts

class TestAddressBook(unittest.TestCase):
    def setUp(self):
        self.contacts = [{"name": "John", "phone": "12345", "email": "john@example.com"}]

    def test_add_contact(self):
        add_contact(self.contacts, "Jane", "67890", "jane@example.com")
        self.assertEqual(len(self.contacts), 2)
        self.assertEqual(self.contacts[-1]['name'], "Jane")

    def test_delete_contact(self):
        delete_contact(self.contacts, 0)
        self.assertEqual(len(self.contacts), 0)

    def test_edit_contact(self):
        edit_contact(self.contacts, 0, "John Doe", "54321", "john_doe@example.com")
        self.assertEqual(self.contacts[0]['name'], "John Doe")
        self.assertEqual(self.contacts[0]['phone'], "54321")

if __name__ == "__main__":
    unittest.main()
