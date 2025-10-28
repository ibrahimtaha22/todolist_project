todolist = []
while (True): 
    command = input (" please insert your command from the following (add, remove, view, exist ) : ")
    if command == "add": 
        task = input ("insert the task to be added : ")
        todolist.append(task)
        print("the task is added.")
    elif command == "view":
        if  not todolist:
            print("there is no task to view!")
        else:
            print(todolist)
            
    elif command == "remove" : 
        if  todolist:
            task = input ("insert the task to be removed : ")
            todolist.remove(task)
            print(todolist)
            print("task removed.")
        else:
            print("there is no task to remove!")
    elif command == "exist" : 
        break

    else : 
        print("invalid option/command")
    






    




