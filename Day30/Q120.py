task_list=[]

def add_task(name):
    """Adds a new task to the list"""

    task_list.append(name)
    print(f"Added: '{name}'")

def remove_task(name):
    """Removes a task by name if it exists"""

    if name in task_list:
        task_list.remove(name)
        print(f"Removed: '{name}'")

    else:
        print(f"Error: '{name}' not found")

def display_task():
    """Displays all current tasks."""
    print("\n---Current Task List---")

    if not task_list:
        print("No tasks available.")

    else:
        for i,task in enumerate(task_list,1):
            print(f"{i}.{task}")
    print("---------\n")

add_task("Finish Python Project")
add_task("Buy books")
add_task("Visit the bank")

display_task()

remove_task("Visit the bank")

display_task()


