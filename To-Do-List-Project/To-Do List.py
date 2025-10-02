tasks = []

# Function to add a task
def add_task():
    task = input("enter your task: ")
    tasks.append(task) # append it to tasks list

# Function to view tasks
def view_tasks():
    print("\n--- Your Tasks ---")
    for index, task in enumerate(tasks):
        print(f"{index + 1}. {task}")

# Function to mark a task as done
def mark_done():
    view_tasks()
    num = input("Enter the task number to mark as done: ")
    try:
        task_index = int(num) - 1
    
        if 0 <= task_index < len(tasks):
            tasks[task_index] = tasks[task_index] + " [DONE]"
            print("Task marked as done!")
        else:
            # This runs if the number is out of range
            print("Invalid task number.")
            
    except ValueError:
        print("Invalid input. Please enter a number.")


# Function to delete a task
def delete_task():
    view_tasks()
    num1 = input("Enter the task number to be deleted: ")
    try:
        task_index1 = int(num1) - 1
        
        # Add the same check here to prevent the bug:
        if 0 <= task_index1 < len(tasks):
            del tasks[task_index1]
            print("Task deleted")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Invalid input. Please enter a number.")
  

# Function to save tasks to file
def save_tasks():
    # 'w' stands for write mode, it will create or overwrite the file
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def load_tasks():
    global tasks
    try:
        with open("tasks.txt", "r") as file:
            tasks = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        # If the file doesn't exist, just start with an empty list
        tasks = []


# Main loop
def main():
    load_tasks()
    while True:
        print("\n--- To-Do List ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Save & Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            save_tasks()
            print("Goodbye friend!")
            break
        else:
            print("Invalid choice. Try again.")

# Run program
main()
