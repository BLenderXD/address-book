import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from address_book import load_contacts, add_contact, delete_contact, edit_contact

# Класс GUI для адресной книги
class AddressBookApp:
    # Конструктор класса
    # @param root Основное окно приложения.
    def __init__(self, root):
        self.root = root
        self.root.title("Address Book")

        # Загружаем контакты
        self.contacts = load_contacts()

        # Создаем интерфейс
        self.create_widgets()

    # Функция для создания виджетов интерфейса
    def create_widgets(self):
        # Заголовок
        self.title_label = tk.Label(self.root, text="Address Book", font=("Arial", 20))
        self.title_label.grid(row=0, column=0, columnspan=4, pady=10)

        # Список контактов (Treeview)
        self.tree = ttk.Treeview(self.root, columns=("Name", "Phone", "Email"), show="headings", height=10)
        self.tree.heading("Name", text="Name")
        self.tree.heading("Phone", text="Phone")
        self.tree.heading("Email", text="Email")
        self.tree.grid(row=1, column=0, columnspan=4, pady=10)

        # Заполнение таблицы контактами
        self.update_contact_list()

        # Поля ввода для имени, телефона и email
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

        # Кнопки
        self.add_button = tk.Button(self.root, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=5, column=0, pady=10)

        self.edit_button = tk.Button(self.root, text="Edit Contact", command=self.edit_contact)
        self.edit_button.grid(row=5, column=1, pady=10)

        self.delete_button = tk.Button(self.root, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=5, column=2, pady=10)

        # Очищаем поля ввода после действия
        self.clear_button = tk.Button(self.root, text="Clear Fields", command=self.clear_fields)
        self.clear_button.grid(row=5, column=3, pady=10)

    # Функция для обновления списка контактов
    def update_contact_list(self):
        # Очищаем таблицу перед обновлением
        for row in self.tree.get_children():
            self.tree.delete(row)

        for contact in self.contacts:
            self.tree.insert("", "end", values=(contact["name"], contact["phone"], contact["email"]))

    # Функция для добавления нового контакта
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

    # Функция для редактирования контакта
    def edit_contact(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Selection Error", "Please select a contact to edit.")
            return

        # Получаем индекс выбранного контакта
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

    # Функция для удаления контакта
    def delete_contact(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Selection Error", "Please select a contact to delete.")
            return

        # Подтверждение перед удалением
        confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this contact?")
        if confirm:
            index = self.tree.index(selected_item)
            delete_contact(self.contacts, index)
            self.update_contact_list()

    # Функция для очистки полей ввода
    def clear_fields(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = AddressBookApp(root)
    root.mainloop()
