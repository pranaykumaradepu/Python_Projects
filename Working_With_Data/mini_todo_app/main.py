import json
import os

task_file = 'tasks.json'

if not os.path.exists(task_file):
    with open(task_file,'w') as file:
        json.dump([],file)

# step 1 : loading data
def loading_data():
    with open(task_file,'r') as file:
        return json.load(file)


# step 2 : save tasks in file
def save_task(tasks):
    with open(task_file,'w') as file:
        json.dump(tasks,file,indent=2)

# step 3 : add task
def add_task():
    task_name = input('Enter task name : ').strip()
    tasks = loading_data()
    tasks.append({'task':task_name,
                  'status': 'incomplete'})
    save_task(tasks)
    print(f'task {task_name} added successfully')

# step 4 : view all tasks 
def view_tasks():
    tasks = loading_data()
    if tasks:
        print('\n To do list : \n')
        for idx,task in enumerate(tasks,start=1):
            print(f'task-{idx}. {task["task"]} : {task["status"]}')
            
    else:
        print('No tasks found')


# step 5 : update task
def update_task_status():
    tasks = loading_data()
    view_tasks()
    try:
        task_index = int(input('Enter task number to update status : '))-1
        if 0 <= task_index < len(tasks):
            new_status = input('Enter the new status ("complete/incomplete") : ').strip()
            tasks[task_index]['status'] = new_status
            save_task(tasks)
            print('Task status updated successfully')
        else:
            print('Invalid task number')
    except ValueError:
        print('Invalid input. Please enter a valid task number.')

# step 6 : delete a task
def delete_task():
    tasks = loading_data()
    view_tasks()
    try:
        task_index = int(input('enter the task number to delete : '))-1
        if 0 <= task_index < len(tasks):
            deleted_task = tasks.pop(task_index)
            save_task(tasks)
            print(f'task {deleted_task["task"]} deleted successfully')
        else:
            print('Invalid task number')
    except ValueError:
        print('Invalid input. Please enter a valid task number.')

# step 7: display menu 
def display_menu():
    print('\n---- Mini To-do App ----')
    print('1. Add Task')
    print('2. View Tasks')
    print('3. Update Task Status')
    print('4. Delete task')
    print('5. Exit')


# step 8 : main program 
def main():
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice (1-5) : "))

            if choice == 1:
                add_task()
            elif choice == 2:
                view_tasks()
            elif choice == 3:
                update_task_status()
            elif choice == 4:
                delete_task()
            elif choice == 5:
                print('Exiting the application')
                break
            else:
                print('Invalid choice. please enter numbers between 1-5 ')
        except ValueError:
            print('Inavlid input enter number 1-5 only')


if __name__ == '__main__':
    main()