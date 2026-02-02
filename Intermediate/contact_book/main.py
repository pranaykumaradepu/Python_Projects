def display():
    print('1. Add new contact ')
    print('2. View all contact ')
    print('3. Search a contact ')
    print('4. Update a contact ')
    print('5. delete a contact ')
    print('6. Exit ')

def view_contact(contacts):
    if not contacts:
        print('-- No contacts found --')
    else:
        for name,phone in contacts.items():
            print(f'''Name : {name} | Phone : {phone}''')

contacts = {}

def main():
    print('--- Contact book ---\n')
    while True:
        display()
        try:
            user_input= int(input('enter your choice : '))
            if user_input == 1:
                name = input('Enter contact name : ')
                phone = int(input('enter contact number :'))
                if name in contacts.keys():
                    print('contact alredy saved')
                else:
                    contacts[name] = phone
                    print(f'new contact {name} and {phone} added sucessfully...')
    
            elif user_input == 2:
                view_contact(contacts)
            
            elif user_input == 3:
                print(f'the phone number{contacts.get(input('Enter the contact name to search : '),'no contact found')}')
            
            elif user_input == 4:
                view_contact(contacts)
                update = input('Enter name to update contact :')
                if name not in contacts:
                    print('Contact not found..')
                else:
                    name = input('Enter new contact name : ')
                    phone = int(input('Enter new contact number :'))
                    print(f'new name {name} and {phone} updated')
            
            elif user_input == 5:
                view_contact(contacts)
                if not contacts:
                    print('no conatcts founf to delte...')
                else:    
                    name = input('enter contact name to delete : ')
                    del contacts[name]
                    print(f'conatct {name} deleted sucessfully...')

            elif user_input == 6:
                print('Thank you...')
                break

        except ValueError:
            print(f'Invalid input try again')
            continue 

main()