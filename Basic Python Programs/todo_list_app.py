# Program to create a To-Do List Application...

def main():
    # Create a list to store tasks
    tasks = []

    def addTask():
        n_task = int(input("How many tasks you want to add: "))
        for i in range(n_task):
            task = input("Enter the Task: ")
            tasks.append({"Task: ": task, "Done": False})
            print("Task Added Successfully!")
        print()

    def showTask():
        if len(tasks) == 0:
            print("No tasks available")
        else:
            for i in range(len(tasks)):
                print()
                print(f"Task {i+1}: {tasks[i]['Task: ']}")
                print(f"Done: {tasks[i]['Done']}")
            print()
                
    def completedTask():
        task_index = int(input("Enter the task number to mark as done: "))
        if task_index > 0 and task_index <= len(tasks):
            tasks[task_index - 1]["Done"] = True
            print("Task marked as done")
        else:
            print("Invalid task number")
        print()

    def deleteTask():
        task_index = int(input("Enter the task number to delete: "))
        if task_index > 0 and task_index <= len(tasks):
            del tasks[task_index - 1]
            print("Task deleted successfully")
        else:
            print("Invalid task number")
        print()


    # Infinite loop to keep the app running until exit
    while True:
        print("================ To Do List ================")
        print("1.Add Task")
        print("2.Show Task")
        print("3.Mark Task as Done")
        print("4.Delete Task")
        print("5.Exit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            addTask()            
        elif choice == 2:
            showTask()
        elif choice == 3:
            completedTask()
        elif choice == 4:
            deleteTask()
        elif choice == 5:
            print("Thank you for using the To Do List App!")
            break
        else:
            print("Invalid input!")

# Execute the program
if __name__ == "__main__":
    main()

