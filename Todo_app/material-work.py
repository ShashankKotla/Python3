import os

TASK_FILE = os.path.abspath('/Users/shashankkotla/Desktop/Todo_app/tasks.txt')
tasks = []

def view():
        if not tasks: # we can write len(tasks) ==0
            print("Tasks not found")
        else:
            for n, task in enumerate(tasks):
                print(f'{n}. {task.strip()}') #strip, each individual task

def add():
    Enter_a_new_task = input("Enter you task: ")
    tasks.append(Enter_a_new_task)
    with open(TASK_FILE, 'a') as file:
        for task in tasks:
            file.write(task + "\n")



def edit():
    view()
    try:
        user_input = int(input("Enter your task number: "))
    except ValueError:
        print("Invalid input.Please enter a number.")
        return

    if 0<=user_input <len(tasks):
        new_task = input("Enter new task to edit existing: ")
        tasks[user_input] = new_task
        with open(TASK_FILE, 'w') as file:
            for task in tasks:
                file.write(task + "\n")
    else:
        print("Invalid task number.")



def delete():
    view()
    try:
        user_input = int(input("Enter a number to delete the existing task: "))
    except ValueError:
        print("Invalid input! please enter a number")
    
    if 0<=user_input <len(tasks):
        del tasks[user_input]
        print("Task deleted!")
        with open(TASK_FILE, 'w') as file:
            for task in tasks:
                file.write(task + '\n')  
    else:
        print("Invalid task number!")

def main():
    while True:
        try:
            with open(TASK_FILE, 'r') as file:
                tasks = file.readlines() #file.readlines(), provides response in list form
        except FileNotFoundError as e: #FileNotFoundError, to check the presence of file 
            print(f"File Not Found Error: {e}")
            with open(TASK_FILE, 'w') as file:
                print('File Created!')
                tasks = []

        print("""
                Todo Options:
                1. view Tasks
                2. Add Task
                3. Edit Task
                4. Delete Task
                5. Exit from Todo!
                """)

        try:
            Choose_Option = int(input("Choose an option for you requirement: "))
        except ValueError:
            print("Invalid input. Please enter a number")
            continue #Go back to the begging of the loop

        if Choose_Option == 1:
            view()
        elif Choose_Option == 2:
            add()
        elif Choose_Option == 3:
            edit()
        elif Choose_Option == 4:
            delete()
        elif Choose_Option == 5:
            print("Exiting. Good Bye!")
            break
        else:
            print('Invalid Choice')



if __name__ == '__main__':
    main()