# phone number is the keys
# name is the value
phone_book = {1111111111: 'Amal', 2222222222: 'Mohammed'}


def add_phone():
    name = input('Enter name:')
    phone_number = input('Enter phone number:')
    phone_number = int(phone_number)
    list_keys = list(phone_book)
    for num in list_keys:
        if phone_number == num:
            msg = 'number already in use'
            return msg
    if len(str(phone_number)) == 10:
        phone_number = int(phone_number)
        phone_book[phone_number] = name
        msg = 'phone added successfully'
        return msg
    else:
        msg = 'wrong phone number'
        return msg

# convert  the  keys and values  of dict to list, phone# is key and name is value


def search_by_name():
    name = input('Enter name:')
    list_keys = list(phone_book.keys())
    list_values = list(phone_book.values())
    if name in list_values:
        key_position = list_values.index(name)
        msg = list_keys[key_position]
        return msg
    else:
        msg = 'Sorry, the number is not found or contact may not exist'
        return msg


def search_by_phone():
    phone_number = input('Enter phone number:')
    phone_number = int(phone_number)
    if len(str(phone_number)) == 10 and isinstance(phone_number, int):
        phone_number = int(phone_number)
        if phone_number in phone_book:
            msg = phone_book[phone_number]
            return msg
        else:
            print('Sorry, the number is not found ')
    else:
        print('This is invalid number')


def print_menu():
    print('Search by phone number: Enter 1')
    print('Search by name: Enter 2')
    print('Add number: Enter 3')
    print('Print menu: Enter 0')


user_input = 0
print_menu()

while user_input != 4:
    user_input = input('Choose a number from 0 to 3:')
    user_input = int(user_input)
    if user_input == 1:
        result = search_by_phone()
        print(result)
    if user_input == 2:
        result = search_by_name()
        print(result)
    if user_input == 3:
        result = add_phone()
        print(result)
    if user_input == 0:
        print_menu()
