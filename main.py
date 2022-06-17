from classes import *

address_book = AddressBook()


# декоратор для функцій, що працюють з даними вводу користувача
def input_error(func):
    def wrapper(*args):
        try:
            return func(*args)
        except (KeyError, ValueError, IndexError):
            return 'Wrong input, try one more time'

    return wrapper


def hello(*args):
    return "How can I help you?"


@input_error
def add(*args):
    name = Name(args[0][0])
    phone = Phone(args[0][1])
    try:
        birthday = Birthday(args[0][2])
    except:
        birthday = None

    if name.value in address_book.data.keys():
        address_book.data[name.value].add_phone(phone)
    else:
        rec = Record(name, phone=phone, birthday=birthday)
        address_book.add_record(rec)
    return f'Contact for {name.value} was added'


@input_error
def change(*args):
    name = Name(args[0][0])
    phone_to_change = Phone(args[0][1])
    phone_new = Phone(args[0][2])
    if name.value in address_book.data.keys():
        address_book.data[name.value].change_phone(phone_to_change, phone_new)
    else:
        raise ValueError('No person with this name in the address book')
    return f'Phone {phone_to_change.value} of {name.value} was changed to {phone_new.value} '


@input_error
def phone(*args):
    name = Name(args[0][0])
    if name.value in address_book.keys():
        list_of_phones = address_book[name.value].phones
        return ', '.join(list_of_phones)


def show_all(*args):
    # # реалізація через записи в адресній книзі
    # str_for_print = ''
    # for k in address_book.values():
    #     str_for_print += str(k) + '\n'
    # return str_for_print

    # реалізація через ітератор - НЕ ВИХОДИТЬ
    block_for_print = address_book.iterator()
    return block_for_print

def exit(*args):
    return "Good bye!"


def days_to_birthday(*args):
    name = Name(args[0][0])
    if name.value in address_book.keys():
        d_t_b = address_book[name.value].days_to_birthday()
        return d_t_b



COMMANDS = {
    hello: ("hello",),
    add: ("add",),
    change: ("change",),
    phone: ("phone",),
    show_all: ("show all",),
    exit: ("good bye", "close", "exit"),
    days_to_birthday: ("days",) #для перевірки функції days_to_birthday класу Records користувач має написати ім'я та телефон в форматі 12.12.12
}


# Парсінг команд від користувача
def processing(customer_input):
    for k in COMMANDS:
        for command in COMMANDS[k]:
            if customer_input.lower().strip().startswith(command):
                list_of_data = customer_input[len(command):].strip().split(" ")
                return k, list_of_data


# Логіка взаємодії з користувачем та виводу результата команд
def main():
    while True:
        customer_input = input(">>>")
        func, data = processing(customer_input)
        print(func(data))
        if func == exit:
            break


if __name__ == '__main__':
    main()
