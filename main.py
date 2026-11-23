packing_list = []

def add_item(list_use, item):
    checking_item = item.strip().lower().replace(' ','')
    clean_item = ' '.join(item.split()).capitalize()
    # error message
    if not checking_item:
        return 'Please add an item'
    if not checking_item.isalpha():
        return 'Your item should not contain number'
    # function
    list_use.append(clean_item)
    return f'{clean_item} has been added'

def remove_item(list_use, item):
    clean_item = ' '.join(item.split()).capitalize()
    # error message
    if not clean_item in list_use:
        return 'Your item must be in the list to remove'
    # function
    while clean_item in list_use:
        list_use.remove(clean_item)
    return f'{clean_item} has been removed'

def view_list(list_use):
    full_list = ['Your current list:']
    for ordered_number, items in enumerate(list_use, 1):
        view = f'{ordered_number}. {items}'
        full_list.append(view)
    return '\n'.join(full_list)

def finish_list(list_use):
    clean_list = ['Your final packing list:']
    for ordered_number, items in enumerate(list_use, 1):
        view = f'{ordered_number}. {items}'
        clean_list.append(view)
    return '\n'.join(clean_list)

print('Packing Manager')
while True:
    prompt1 = input('What would you like to do? (Add, Remove, View, or Finish)  ').strip().lower().replace(' ', '')
    if prompt1 == 'add':
        add = input('What would you like to add?  ')
        message = add_item(packing_list, add)
        print(message)
    elif prompt1 == 'remove':
        remove = input('What would you like to remove?  ')
        message = remove_item(packing_list, remove)
        print(message)
    elif prompt1 == 'view':
        if not packing_list:
            print('Your list is empty')
        else:
            print(view_list(packing_list))
    elif prompt1 == 'finish':
        if not packing_list:
            print('Your list is empty')
        else:
            print(finish_list(packing_list))
        break
    else:
        print('Please provide the correct input!')
        continue