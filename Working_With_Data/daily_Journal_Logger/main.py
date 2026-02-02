import datetime

journal_file = 'journal.txt'
password = 'journal123'  # basic password

def authenticate():
    attempts = 3
    while attempts > 0:
        entered_password = input('Enter your password : ').lower()
        if entered_password == password:
            print('Access granted ✅\n')
            return True
        else:
            attempts -= 1
            print(f'Wrong Password ❌ Attempts left: {attempts}')
    print('Acess Denied. Exiting program')
    return False

# creating a function to add new entrty 
def add_new_entry():
    entry_text = input('Write your journal entry : ')

    try:
        with open(journal_file,'a+') as file:

            file.seek(0)
            entries = file.readlines()

            # Add header only if file is empty
            if len(entries) == 0:
                file.write('---- Daily Journal Entries ----\n')
                file.write('[Number of Entries] | [Date] | [Entry Text]\n')
                file.write('----------------------------------\n')

            # count only actual entries
            entry_lines = [entry for entry in entries if entry.startswith('[Entry-')]
            print( entry_lines)
            entry_number = len(entry_lines) + 1

            # get current date
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d")
            
            # writes content in txt file   
            file.write(f'[Entry-{entry_number}] | {timestamp} | {entry_text}\n')
        print('New journal entry added sucessfully ✅')
    
    except PermissionError:
        print('Permission denied while writing to the journal file')
    
# viewing all entries 
def view_all_entries():
    try:
        with open(journal_file,'r') as file:
            lines = file.readlines()

            entries = [line.strip() for line in lines if line.startswith('[Entry-')]
            if not entries:
                print('No journal entries found')
                return
            
            print(f'{lines[1]}\n{lines[2]}')
            for entry in entries:
                print(entry.strip())
    except FileNotFoundError:
          print(f'File {journal_file} not found')

# viewing  entry with specific keyword 
def specific_entry():
    keyword = input('Enter keyword to search : ').lower()
    found = False 
    try:
        with open(journal_file,'r') as file:
            for entry in file:
                if keyword in entry.lower():
                    print(entry.strip())
                    found = True
        if not found:
            print(f'No entries found cotaining {keyword}')
    except FileNotFoundError:
        print('Journal file not found. Add an entry first')

def show_menu():
    print('\n ----- Journal Entry Application ----')    
    print('1. Add New Entry ')
    print('2. View All Entries ')
    print('3. Search Entry Keyword  entry ')
    print('4. Exit')


def main():

    # if not authenticate():
    #     return 
    
    while True:
        show_menu()
        try:
            user_input = int(input('Enter your choice (1-4): '))
            if user_input == 1:
                add_new_entry()
            elif user_input == 2:
                view_all_entries()
            elif user_input == 3:
                specific_entry()
            elif user_input == 4:
                print('Exiting the application.')
                break
            else:
                print('Invalid choice.please select between 1-4 ')
        except ValueError:
            print('Invalid Choice ! Please enter a number between 1 and 4.')
    
if __name__ == '__main__':
    main()