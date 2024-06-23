import list_module
from list import ToDoList

def main():
    while True:
        print("Welcome to the py todo list \n")
        print("1. Add a task with title and description.")
        print("2. Remove a task by title.")
        print("3. Update a task's description or status.")
        print("4. List all tasks. ")
        print("5. Filter tasks by status (e.g., pending, completed).")
        print("6. Exit")
        
        choice = int(input("Select what to do from the list: \n"))
        
        if choice == 1:
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            status = input("Enter task status: ")
            task = ToDoList(title, description, status)
            list_module.add_task(task)
        elif choice == 2:
            title = input("Enter the title for the task you want to remove: ")
            list_module.remove_task(title)
        elif choice == 3:
            title = input("Enter task title to update: ")
            description = input("Enter new description (or press Enter to skip): ")
            status = input("Enter new status (pending/completed, or press Enter to skip): ")
            list_module.update_task(title, description, status)
        elif choice == 4:
            tasks = list_module.list_all_tasks()
            if not tasks:
                print(">> No tasks to do")
            else:
                for task in tasks:
                    print("Task name: ", task) 
        elif choice == 5:
            status = input("Enter status to filter by (pending/completed): ")
            tasks = list_module.filter_tasks_by_status(status)
            for task in tasks:
                print(task)   
        elif choice == 6:
            break
        else:
            print("Invalid choice, please try again.")         
               
if __name__ == "__main__":
    main()