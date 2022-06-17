from collections import UserDict
from datetime import datetime, timedelta


# Не дуже зрозуміло, нащо цей додатковий клас, проте за умовою домашки був потрібний, тому він тут є))
class Field:
    def __init__(self, value: str):
        self.value = None
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    # перевірка на вірність значень
    # критерії перевірки: телефон має складатись з 9 цифр
    def __init__(self, value):
        if value.isdigit() and len(value) == 9:
            super().__init__(value)
        else:
            print('Wrong format of Phone, 9 digits needed')
            raise ValueError


class Birthday(Field):
    # перевірка на вірність значень
    # критерії перевірки: формат dd.mm.yyyy
    def __init__(self, value):
        def validate(value):
            try:
                print(value)
                datetime.strptime(value, '%m.%d.%Y')
                return True
            except ValueError:
                return False
        if validate(value):
            super().__init__(value)
        else:
            print('Wrong format of Phone, 9 digits needed')
            raise ValueError


class Record:
    # Ініціалізуємо запис, щоб в ній зберігалися обов'язковий параметр ім'я, необов'язковий телефон,
    # а також створюємо список з об'єктів - телефонів
    # а також, зберігання необов'язкового поля birthday та
    #  додаткову функцію, що рахує кількість днів до наступного дня народження

    def __init__(self, name: Name, phone=None, birthday=None):
        self.name = name
        self.phones = []
        if phone is not None:
            self.phones.append(phone.value)
        if birthday is not None:
            self.birthday = birthday


    # Фукція для додавання нового телефону для юзера
    def add_phone(self, ph: Phone):
        self.phones.append(ph.value)

    # Функція для зміни телефона на новий
    def change_phone(self, ph: Phone, new_ph: Phone):
        i = 0
        while i < len(self.phones):
            if self.phones[i] == ph.value:
                self.phones[i] = new_ph.value
                break
            else:
                i += 1

    # Функція, яка повертає кількість днів до наступного дня народження
    def days_to_birthday(self):
        now_day = datetime.now()

        bd_date = datetime.strptime(self.birthday.value, '%d.%m.%Y')
        bd_day, bd_month = bd_date.day, bd_date.month
        bd_this_year = datetime(day=bd_day, month=bd_month, year=now_day.year)
        bd_next_year = datetime(day=bd_day, month=bd_month, year=now_day.year + 1)
        if bd_this_year < now_day:
            delta = bd_next_year - now_day
        else:
            delta = bd_this_year - now_day
        return delta.days

    def __str__(self):
        return '{:<10}'.format(self.name.value) + ':' + ', '.join(self.phones)


class AddressBook(UserDict):
    N = 5

    def add_record(self, rec: Record):
        k, i = rec.name.value, rec
        self.data[k] = i

    def iterator(self):
        block = ''
        string_counter = 0
        for rec in self.data.values():
            string_counter += 1
            block += str(rec) + '\n'
            if string_counter == self.N:
                yield block
                string_counter = 0
        yield block





