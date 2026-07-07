# Study Dashboard
# Version 0.1

# Features:
# - View tasks
# - Add tasks
# - Complete tasks
# - Quit

todo_list = []
   
def main():
    while True:
        print("Welcome to the Study Dashboard!")
    
        print("Please select an option:")
        print("1. Add a new task ")
        print("2. View today's todo list")
        print("3. Mark a task as complete")
        print("4. Quit")
    
        choice = input("Enter your choice (1-4): ")
    
        if choice == "1":
            add_task()
        elif choice == "2":
            display_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            print("Goodbye!")
            break


def add_task():
    new_task = input("Enter the new task: ")
    todo_list.append(new_task)
    
    add_choice = input("Task successfully added! Would you like to add another task? (y/n): ")
    if add_choice == "y":
        new_choice = input("Enter the new task: ")
        todo_list.append(new_choice)
    elif add_choice == "n": 
        print("Returning to main menu...\n")
    else:
        print("Invalid input. Returning to main menu...\n")
    
def display_tasks():
    if not todo_list:
        print("No tasks for today!")
        return
    else: 
        print("Today's todo list: ")
        for i in range(len(todo_list)):
            print(i+1, todo_list[i])
        
    user_input = input("Enter 'm' to return to main menu: ")
    if user_input == "m":
        print("Returning to main menu...\n")
    else:
        print("Invalid input. Please try again.\n")
        display_tasks()

def complete_task():
    if not todo_list:
        print("No tasks for today!\n")
        return
    else:
        print("Today's todo list: ")
        for i in range(len(todo_list)): 
            print(i+1, todo_list[i]) 
    
    user_input = input("Enter the task you want to mark as complete (number): ")
    task_index = int(user_input) - 1 
    todo_list.pop(task_index)
    print("Task marked as complete!")
    
    user_input = input("Would you like to mark another task as complete? (y/n): ")
    if user_input == "y":
        complete_task()
    elif user_input == "n": 
        print("Returning to main menu...\n")
    else:
        print("Invalid input. Returning to main menu...\n")

main()

