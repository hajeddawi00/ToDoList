tasks: list = []

while True:
    print('\n===== To-Do List =====')
    print('1. Add Task')
    print('2. View Tasks')
    print('3. Mark Task as Complete')
    print('4. Delete Task')
    print('5. Exit \n')

    user_choice = input('Enter your choice: ')

    if user_choice == '1':
        label: str = input('Enter task name: ')
        tasks.append(f'[ ] {label}')  # Fix empty brackets formatting
        print('Task added!\n')

    elif user_choice == '2':
        if tasks:
            print('Your Tasks:')
            for i, task in enumerate(tasks, start=1):
                print(f'{i}. {task}')
        else:
            print('No tasks available.\n')

    elif user_choice == '3':
        if tasks:
            try:
                task_number = int(input('Enter task number to mark as complete: '))
                if 1 <= task_number <= len(tasks):
                    tasks[task_number - 1] = tasks[task_number - 1].replace('[ ]', '[X]', 1)
                    print('Task marked as complete!')
                else:
                    print('Invalid task number!')
            except ValueError:
                print('Please enter a valid number!')
        else:
            print('No tasks available to mark.\n')

    elif user_choice == '4':
        if tasks:
            try:
                deleted_task = int(input('Enter task number to delete: '))
                if 1 <= deleted_task <= len(tasks):
                    tasks.pop(deleted_task - 1)
                    print('The task has been deleted successfully..')
                else:
                    print('Invalid task number!')
            except ValueError:
                print('Please enter a valid number!')
        else:
            print('No tasks available to delete.\n')

    elif user_choice == '5':
        print('Exiting... Goodbye!')
        break

    else:
        print(f'Oops.. "{user_choice}" is an invalid input! \n')
