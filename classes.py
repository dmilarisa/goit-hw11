from collections import UserDict
from datetime import datetime, timedelta


# Не дуже зрозуміло, нащо цей додатковий клас, проте за умовою домашки був потрібний, тому він тут є))
class Field:
    def __init__(self, value: str):
        self._value = None
        self.value = value

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        self._value = value


class Name(Field):
    pass


class Phone(Field):
    # перевірка на вірність значень
    # критерії перевірки: телефон має складатись з 9 цифр
    # def __init__(self, value):
        
    @Field.value.setter
    def value(self, value):
        if value.isdigit() and len(value) == 9:
            self._value = value
        else:
            print('Wrong format of Phone, 9 digits needed')
            raise ValueError


class Birthday(Field):
    # перевірка на вірність значень
    # критерії перевірки: формат dd.mm.yyyy
    # def __init__(self, value):
    #     def validate(value):
    #         try:
    #             print(value)
    #             datetime.strptime(value, '%m.%d.%Y')
    #             return True
    #         except ValueError:
    #             return False
    #     if validate(value):
    #         super().__init__(value)
    #     else:
    #         print('Wrong format of Phone, 9 digits needed')
    #         raise ValueError
    @Field.value.setter
    def value(self, value):
        try:
            print(value)
            self._value = datetime.strptime(value, '%m.%d.%Y').date()
            return True
        except ValueError:
            return False
        # if validate(value):
        #     super().__init__(value)
        # else:
        #     print('Wrong format of Phone, 9 digits needed')
        #     raise ValueError


class Record:
    # Ініціалізуємо запис, щоб в ній зберігалися обов'язковий параметр ім'я, необов'язковий телефон,
    # а також створюємо список з об'єктів - телефонів
    # а також, зберігання необов'язкового поля birthday та
    #  додаткову функцію, що рахує кількість днів до наступного дня народження

    def __init__(self, name: Name, phone: Phone= None, birthday: Birthday= None):
        self.name = name
        self.phones = []
        if phone is not None:
            self.phones.append(phone.value) # Додавати потрібно не value а саме об'єкт!
        # if birthday is not None: # Поле все одно повинно існувати
        self.birthday = birthday


    # Фукція для додавання нового телефону для юзера
    def add_phone(self, ph: Phone):
        self.phones.append(ph.value)  # Додавати потрібно не value а саме об'єкт!

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
        if not self.birthday:
            return None
        
        now_day = datetime.now()
        
        # bd_date = datetime.strptime(self.birthday.value, '%d.%m.%Y') # Чому відразу тут не зберігати datetime об'єкт?
        bd_date = self.birthday.value
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

    def add_record(self, rec: Record):
        k, i = rec.name.value, rec
        self.data[k] = i

    def iterator(self, rec_num = 2):
        block = ''
        string_counter = 0
        for rec in self.data.values():
            string_counter += 1
            block += str(rec) + '\n'
            if string_counter == rec_num:
                block += '-' * 40
                yield block
                string_counter = 0
                block = ''
        yield block


if __name__ == "__main__":
    r1 = Record(Name("Billy"), Phone("663456789"))
    r2 = Record(Name("Susanna"), Phone("987653434"), Birthday("06.25.1995"))
    r3 = Record(Name("Jonny"), Phone("675433434"))
    
    ab = AddressBook()
    
    ab.add_record(r1)
    ab.add_record(r2)
    ab.add_record(r3)
    
    print(r2.days_to_birthday())
    
    print(r1.days_to_birthday())
    
    print(ab)
    
    for rec in ab.iterator():
        print(rec)

    for rec in ab.iterator(3):
        print(rec)

    for rec in ab.iterator(1):
        print(rec)
