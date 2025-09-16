def task():
    tasks = []
    print("---- To-Do List ----")
    
    total_task = int(input("Enter today's task count = "))
    for i in range(1,total_task + 1):
        task_name = input(f"Enter task {i}: ")
        tasks.append(task_name)
        
    print(f"Today's tasks are : \n{tasks}")
    
    while True:
        print("\n Enter an option number from below: ")
        operation = int(input("1 - Add\n2 - Update\n3 - Delete\n4 - View\n5 - Exit/Stop\n Enter your choice: "))
        
        if operation == 1:
            add = input("Enter a task: ")
            tasks.append(add)
            print(f"Task {add} added to today's list")
        
        elif operation == 2:
            update = input("Enter task to be updated: ")
            if update in tasks:
                up = input("Enter updated task: ")
                ind = tasks.index(update)
                tasks[ind] = up
                print(f"Task {update} has been updated by {up}.")
            else:
                print(f"Task {update} not found")
        
        elif operation == 3:
            delete = input("Enter a task to delete: ")
            if delete in tasks:
                tasks.remove(delete)
                print(f"Task {delete} has been deleted.")
            else:
                print(f"Task {delete} not found")
                
        elif operation == 4:
            print(f"Today's tasks are : \n{tasks}")
            
        elif operation == 5:
            print("Closing the program...")
            break
        
        else:
            print("Invalid input. Please enter a number between 1 to 5.")

task() 