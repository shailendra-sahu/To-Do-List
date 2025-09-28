def add_task():
    # Read existing tasks to find the last number
    try:
        with open('todolist.txt', 'r') as f:
            tasks = f.readlines()
        if tasks:
            last_num = int(tasks[-1].split('.', 1)[0])  # get last number
        else:
            last_num = 0
    except FileNotFoundError:
        last_num = 0  # no file means start from 0

    with open('todolist.txt', 'a') as f:
        total_task = int(input("Enter how many tasks you want to add: "))
        for i in range(1, total_task + 1):
            task_name = input(f"Enter task {last_num + i}: ")
            f.write(f"{last_num + i}.{task_name}\n")
        print("Tasks added successfully.\n")


def update_task():
    try:
        with open('todolist.txt','r') as f:
            tasks=f.readlines()
        if not tasks:
            print("\nNo tasks found. Your to-do list is empty")
            return
        print("\nYour to-do list:")
        for task in tasks:
            print(task,end='')
        task_num=int(input("\nEnter the task number you want to update: "))
        if 1<=task_num<=len(tasks):
            new_task=input("Enter update task:")
            tasks[task_num-1]=f'{task_num}.{new_task}\n'
            with open('todolist.txt','w') as f:
                f.writelines(tasks)
            print("Task updated successfully")
        else:
            print("invalid task number")
    except FileNotFoundError:
        print("\nNo tasks found. Your to-do list is empty.")

def del_task():
    try:
        with open('todolist.txt', 'r') as f:
            tasks = f.readlines()
        if not tasks:
            print("\nYour to-do list is empty. Nothing to delete.")
            return

        print("\nYour to-do list:")
        for task in tasks:
            print(task, end='')

        task_num = int(input("\nEnter the task number you want to delete: "))
        if 1 <= task_num <= len(tasks):
            tasks.pop(task_num - 1)
            with open('todolist.txt', 'w') as f:
                f.writelines(tasks)
            print("Task deleted successfully.")
        else:
            print("Invalid task number.")
    except FileNotFoundError:
        print("\nNo tasks found. Your to-do list is empty.")

def view_task():
    try:
        with open('todolist.txt','r') as f:
            content=f.read()
            if content.strip():
                print("\nYour To-Do List:")
                print(content)
            else:
                print("\nYour to-do list is empty.")
    except FileNotFoundError:
        print("\nNo tasks found. Your to-do list is empty.")

while True:
    print("\n-----Welcome to To Do List App -----")
    print("Enter 1- Add Task")
    print("Enter 2- Update Task")
    print("Enter 3- Delete Task")
    print("Enter 4- View Task")
    print("Enter 5- Exit Tasks")
    choice=int(input("Enter Choice : "))
    if choice==1:
        add_task()

    elif choice==2:
        update_task()

    elif choice==3:
        del_task()

    elif choice==4:
        view_task()

    elif choice == 5:
        print("Goodbye! 👋")
        break
    else:
        print("Invalid choice. Please enter a number between 1-5.")