phonebook_dictionary = {}
contact_info = input().split("-")
while len(contact_info) > 1:
    person = contact_info[0]
    number = contact_info[1]
    phonebook_dictionary[person] = number
    contact_info = input().split("-")
number_of_contacts_to_search = int(contact_info[0])
for _ in range(number_of_contacts_to_search):
    contact_name = input()
    if contact_name not in phonebook_dictionary.keys():
        print(f'Contact {contact_name} does not exist.')
    else:
        print(f'{contact_name} -> {phonebook_dictionary[contact_name]}')