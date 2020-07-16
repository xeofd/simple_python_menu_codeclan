# Main app file

# Import functions
import modules.task_list as t_list
import modules.output as dumb

# Main loop
while (True):
    dumb.print_menu()
    option = input("Select an option 1, 2, 3, 4, 5 or (Q)uit: ")
    if (option.lower() == 'q'):
        break
    if option == '1':
        dumb.print_list(t_list.tasks)
    elif option == '2':
        dumb.print_list(t_list.get_uncompleted_tasks(t_list.tasks))
    elif option == '3':
        dumb.print_list(t_list.get_completed_tasks(t_list.tasks))
    elif option == '4':
        description = input("Enter task description to search for: ")
        task = t_list.get_task_with_description(t_list.tasks, description)
        if task != "Task Not Found":
            t_list.mark_task_complete(task)
    elif option == '5':
        time = int(input("Enter task duration: "))
        dumb.print_list(t_list.get_tasks_taking_longer_than(t_list.tasks, time))
    elif option == '6':
        description = input("Enter task description to search for: ")
        print(t_list.get_task_with_description(t_list.tasks, description))
    elif option == '7':
        description = input("Enter description: ")
        time_taken = int(input("Enter time taken: "))
        task = t_list.create_task(description, time_taken)
        t_list.tasks.append(task)
    else:
        print("Invalid Input - choose another option")
