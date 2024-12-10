"""
@file address_book.py
@brief This file contains functions for managing contacts in an address book.
"""

import csv

# @brief Loads contacts from a CSV file.
# @param filename The name of the CSV file to load contacts from.
# @return A list of contacts.
def load_contacts(filename="contacts.csv"):
    contacts = []
    try:
        with open(filename, mode="r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                contacts.append(row)
    except FileNotFoundError:
        pass  # Return an empty list if the file does not exist.
    return contacts

# @brief Saves contacts to a CSV file.
# @param contacts The list of contacts to save.
# @param filename The name of the CSV file to save contacts to.
def save_contacts(contacts, filename="contacts.csv"):
    with open(filename, mode="w", newline="") as file:
        fieldnames = ["name", "phone", "email"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(contacts)

# @brief Adds a new contact to the list.
# @param contacts The list of contacts.
# @param name The name of the contact.
# @param phone The phone number of the contact.
# @param email The email address of the contact.
def add_contact(contacts, name, phone, email):
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)

# @brief Deletes a contact from the list by index.
# @param contacts The list of contacts.
# @param index The index of the contact to delete.
def delete_contact(contacts, index):
    del contacts[index]
    save_contacts(contacts)

# @brief Edits a contact in the list.
# @param contacts The list of contacts.
# @param index The index of the contact to edit.
# @param name The new name of the contact.
# @param phone The new phone number of the contact.
# @param email The new email address of the contact.
def edit_contact(contacts, index, name, phone, email):
    contacts[index] = {"name": name, "phone": phone, "email": email}
    save_contacts(contacts)
