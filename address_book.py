import csv

# Функция для загрузки контактов из CSV файла
# @param filename Имя CSV файла.
# @return Список контактов.
def load_contacts(filename="contacts.csv"):
    contacts = []
    try:
        with open(filename, mode="r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                contacts.append(row)
    except FileNotFoundError:
        pass  # Если файл не найден, возвращаем пустой список
    return contacts

# Функция для сохранения контактов в CSV файл
# @param contacts Список контактов для сохранения.
# @param filename Имя CSV файла.
def save_contacts(contacts, filename="contacts.csv"):
    with open(filename, mode="w", newline="") as file:
        fieldnames = ["name", "phone", "email"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(contacts)

# Функция для добавления нового контакта
# @param contacts Список контактов.
# @param name Имя контакта.
# @param phone Номер телефона контакта.
# @param email Электронная почта контакта.
def add_contact(contacts, name, phone, email):
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)

# Функция для удаления контакта
# @param contacts Список контактов.
# @param index Индекс контакта для удаления.
def delete_contact(contacts, index):
    del contacts[index]
    save_contacts(contacts)

# Функция для редактирования контакта
# @param contacts Список контактов.
# @param index Индекс контакта для редактирования.
# @param name Новое имя контакта.
# @param phone Новый номер телефона контакта.
# @param email Новая электронная почта контакта.
def edit_contact(contacts, index, name, phone, email):
    contacts[index] = {"name": name, "phone": phone, "email": email}
    save_contacts(contacts)
