#АДРЕСНА КНИГА

from collections import UserDict

class AddressBook(UserDict):
    def add_record(self, record):
        key = record.name.value
        self.data[key] = record

    def remove_record(self, name):
        if name in self.data:
            del self.data[name]

    def find_records(self, **search_criteria):
        result = []
        for record in self.data.values():
            name_match = search_criteria.get('name') is None or record.name.value == search_criteria['name']
            phones_match = search_criteria.get('phones') is None or search_criteria['phones'] in record.phones.value
            if name_match and phones_match:
                result.append(record)
        return result

    def __str__(self):
        book_str = "\n".join(f"{name}: {record}" for name, record in self.data.items())
        return book_str


class Record:
    def __init__(self, name, *phones):
        self.name = Name(name)
        self.phones = Phone()
        for phone in phones:
            self.phones.add_number(phone)

    def add_phone_number(self, number):
        self.phones.add_number(number)

    def remove_phone_number(self, number):
        self.phones.remove_number(number)

    def change_phone_number(self, old_number, new_number):
        self.phones.change_number(old_number, new_number)

    def __str__(self):
        phones_str = ', '.join(str(phone) for phone in self.phones.value)
        return f"Name: {self.name.value}, Phones: {phones_str}"

class Field:
    def __init__(self, value=None):
        self.value = value

    def update(self, new_value):
        self.value = new_value

    def __str__(self):
        return str(self.value)

class Phone(Field):
    def __init__(self, value=None):
        if value is None:
            value = []
        super().__init__(value)

    def add_number(self, number):
        self.value.append(number)

    def remove_number(self, number):
        if number in self.value:
            self.value.remove(number)
            return True
        return False

    def change_number(self, old_number, new_number):
        if old_number in self.value:
            index = self.value.index(old_number)
            self.value[index] = new_number

class Name(Field):
    def __init__(self, value):
        super().__init__(value)


if __name__=="__main__":

    # Створення об'єкту класу AddressBook
    book = AddressBook()
    record1 = Record("John", "12345")
    record2 = Record("Jane", "67890")
    #
    # Виклик методів класу AddressBook
    book.add_record(record1)
    book.add_record(record2)

    # Виведення результатів
    print("Address Book:")
    print(book)

    # Виклик методу find_records з критеріями пошуку

    # Пошук записів з ім'ям "John" та номером "12345"
    result = book.find_records(name="John", phones="12345")

    # Виведення результатів
    print("\nFind Records:")
    for record in result:
        print(record)

    # Пошук записів з ім'ям "John" (без вказування номеру)
    result = book.find_records(name="John")

    # Виведення результатів
    print("\nFind Records with name 'John':")
    for record in result:
        print(record)

    # Пошук записів з номером "12345" (без вказування імені)
    result = book.find_records(phones="12345")

    # Виведення результатів
    print("\nFind Records with phone '12345':")
    for record in result:
        print(record)

    #Перевірка методів класу Record

    #Cтворення об'єкта класу Record
    record1 = Record("John", "12345", "67890")

    # Виклик методу add_phone_number
    record1.add_phone_number("55555")
    # Виведення результатів
    print(record1)

    # Виклик методу remove_phone_number
    record1.remove_phone_number("678990")
    # Виведення результатів
    print(record1)

    # Виклик методу change_phone
    record1.change_phone_number("12345", "99999")
    # Виведення результатів
    print(record1)

    #Перевірка класу Field

    # Створення об'єкта класу Field
    field = Field()
    # Виведення значення за допомогою методу __str__
    print("Field value:", field)

    # Оновлення значення за допомогою методу update
    field.update("New Value")
    print("Updated field value:", field)


    #Перевірка класу Phone

    # Створення об'єкта класу Phone
    phone = Phone()

    # Виведення значення за допомогою методу __str__
    print("Phone value:", phone)

    # Додавання номера за допомогою методу add_number
    phone.add_number("12345")
    phone.add_number("67890")

    # Виведення значення після додавання номерів
    print("Phone value after adding numbers:", phone)

    # Зміна телефону
    phone.change_number("67890", "2352352345")

    # Виведення значення після зміні номера
    print("Phone value after changing number:", phone)

    # Видалення номера за допомогою методу remove_number
    phone.remove_number("12345")

    # Виведення значення після видалення номера
    print("Phone value after removing number:", phone)

    #Перевірка класу Name

    # Створення об'єкта класу Name
    name = Name("John Doe")

    # Виведення значення за допомогою методу __str__
    print("Name value:", name)

    # Оновлення значення за допомогою методу update
    name.update("Jane Doe")
    print("Updated name value:", name)