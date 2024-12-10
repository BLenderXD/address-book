"""
@file gui.py
@brief This file contains the graphical user interface (GUI) for managing the address book.
"""

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from address_book import load_contacts, add_contact, delete_contact, edit_contact

# @class AddressBookApp
# @brief A class representing the GUI for the address book application.
class AddressBookApp:
    # @brief Initializes the application.
    # @param root The main window object for the application.
    def __init__(self, root):
        self.root = root
        self.root.title("Address Book")

        # Load contacts from file
        self.contacts = load_contacts()

        # Create the GUI widgets
        self.create_widgets()

    # @brief Creates the widgets for the application.
    def create_widgets(self):
        # Title label
        self.title_label = tk.Label(self.root, text="Address Book", font=("Arial", 20))
        self.title_label.grid(row=0, column=0, columnspan=4, pady=10)

        # Treeview for displaying contacts
        self.tree = ttk.Treeview(self.root, columns=("Name", "Phone", "Email"), show="headings", height=10)
        self.tree.heading("Name", text="Name")
        self.tree.heading("Phone", text="Phone")
        self.tree.heading("Email", text="Email")
        self.tree.grid(row=1, column=0, columnspan=4, pady=10)

        # Populate treeview with contacts
        self.update_contact_list()

        # Entry fields
        self.name_label = tk.Label(self.root, text="Name:")
        self.name_label.grid(row=2, column=0, pady=5)
        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(row=2, column=1, pady=5)

        self.phone_label = tk.Label(self.root, text="Phone:")
        self.phone_label.grid(row=3, column=0, pady=5)
        self.phone_entry = tk.Entry(self.root)
        self.phone_entry.grid(row=3, column=1, pady=5)

        self.email_label = tk.Label(self.root, text="Email:")
        self.email_label.grid(row=4, column=0, pady=5)
        self.email_entry = tk.Entry(self.root)
        self.email_entry.grid(row=4, column=1, pady=5)

        # Buttons
        self.add_button = tk.Button(self.root, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=5, column=0, pady=10)

        self.edit_button = tk.Button(self.root, text="Edit Contact", command=self.edit_contact)
        self.edit_button.grid(row=5, column=1, pady=10)

        self.delete_button = tk.Button(self.root, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=5, column=2, pady=10)

        self.clear_button = tk.Button(self.root, text="Clear Fields", command=self.clear_fields)
        self.clear_button.grid(row=5, column=3, pady=10)

    # @brief Updates the treeview with the contact list.
    def update_contact_list(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        for contact in self.contacts:
            self.tree.insert("", "end", values=(contact["name"], contact["phone"], contact["email"]))

    # @brief Adds a new contact to the list.
    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()

        if not name or not phone or not email:
            messagebox.showwarning("Input Error", "Please fill in all fields!")
            return

        add_contact(self.contacts, name, phone, email)
        self.update_contact_list()
        self.clear_fields()

    # @brief Edits a selected contact.
    def edit_contact(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Selection Error", "Please select a contact to edit.")
            return

        index = self.tree.index(selected_item)
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()

        if not name or not phone or not email:
            messagebox.showwarning("Input Error", "Please fill in all fields!")
            return

        edit_contact(self.contacts, index, name, phone, email)
        self.update_contact_list()
        self.clear_fields()

    # @brief Deletes a selected contact.
    def delete_contact(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Selection Error", "Please select a contact to delete.")
            return

        confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this contact?")
        if confirm:
            index = self.tree.index(selected_item)
            delete_contact(self.contacts, index)
            self.update_contact_list()

    # @brief Clears the input fields.
    def clear_fields(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = AddressBookApp(root)
    root.mainloop()
