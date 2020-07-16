# Main app file

# Import functions
import modules.task_list as t_list
import modules.output as dumb
import data.task_list as data
import modules.modules.input as user_input

# Main loop
while (True):
    dumb.print_menu()
    option = input("Select an option 1, 2, 3, 4, 5 or (Q)uit: ")
    if (option.lower() == 'q'):
        break
    if option == '1':
        dumb.print_list(data.tasks)
    elif option == '2':
        dumb.print_list(t_list.get_uncompleted_tasks(data.tasks))
    elif option == '3':
        dumb.print_list(t_list.get_completed_tasks(data.tasks))
    elif option == '4':
        task = t_list.get_task_with_description(data.tasks, user_input.desc_input())
        if task != "Task Not Found":
            t_list.mark_task_complete(task)
    elif option == '5':
        dumb.print_list(t_list.get_tasks_taking_longer_than(data.tasks, user_input.task_time()))
    elif option == '6':
        print(t_list.get_task_with_description(data.tasks, user_input.desc_input()))
    elif option == '7':
        task = t_list.create_task(user_input.desc_input(), user_input.task_time())
        data.tasks.append(task)
    else:
        print("Invalid Input - choose another option")
