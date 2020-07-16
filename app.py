# Main app file

# Import functions
import task_list
import output

# Main loop
while (True):
    output.print_menu()
    option = input("Select an option 1, 2, 3, 4, 5 or (Q)uit: ")
    if (option.lower() == 'q'):
        break
    if option == '1':
        output.print_list(task_list.tasks)
    elif option == '2':
        output.print_list(task_list.get_uncompleted_tasks(task_list.tasks))
    elif option == '3':
        output.print_list(task_list.get_completed_tasks(task_list.tasks))
    elif option == '4':
        description = input("Enter task description to search for: ")
        task = task_list.get_task_with_description(task_list.tasks, description)
        if task != "Task Not Found":
            task_list.mark_task_complete(task)
    elif option == '5':
        time = int(input("Enter task duration: "))
        output.print_list(task_list.get_tasks_taking_longer_than(task_list.tasks, time))
    elif option == '6':
        description = input("Enter task description to search for: ")
        print(task_list.get_task_with_description(task_list.tasks, description))
    elif option == '7':
        description = input("Enter description: ")
        time_taken = int(input("Enter time taken: "))
        task = task_list.create_task(description, time_taken)
        tasks.append(task)
    else:
        print("Invalid Input - choose another option")
