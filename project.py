# phone number is the keys
# name is the value
phone_book = {'1111111111': 'Amal', '2222222222': 'Mohammed'}


def add_phone():
    name = input('Enter name:')
    phone_number = input('Enter phone number:')
    list_keys = list(phone_book)
    for num in list_keys:
        print(num)
        if num == phone_number:
            msg = 'number already in use'
            return msg
        else:
            phone_book['phone_number'] = name
            print('phone added successfully')

# convert  the  keys and values  of dict to list, phone# is key and name is value


def search_by_name():
    name = input('Enter name:')
    list_keys = list(phone_book.keys())
    list_values = list(phone_book.values())
    for value in list_values:
        if name == value:
            print(value.index(name))
        else:
            print('Sorry, the number is not found ')


def search_by_phone():
    phone_number = input('Enter phone number:')
    if phone_number == 10 and isinstance(phone_number, int):
        if phone_book['phone_number'] in phone_book:
            print(phone_book['phone_number'])
        else:
            print('Sorry, the number is not found ')
    else:
        print('This is invalid number')


# print('search by phone number: Enter 1')
# print('search by name: Enter 2')
# print('add number: Enter 3')
# user_input = input('Enter a number:')
# user_input = int(user_input)

# while user_input <= 3:
#     if user_input == 1:
#         search_by_phone()
#     if user_input == 2:
#         search_by_name()
#     if user_input == 3:
#         result = add_phone()
#         print(result)
