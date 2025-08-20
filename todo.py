tasks = []
pin_enabled = False
pin = None

def check_pin():
    entered = input("Enter PIN: ")
    return entered == pin

while True:
    print("\n To-Do-List App")
    
    
    options= ["Add tasks", "Inspect Tasks", "Lock/unlock Your tasks", "Delete tasks", "Quit"]

    for n, option in enumerate(options, start=1):
        print(f"{n}.{option}")




    choose = input("Choose an option: ")

    if choose == '1':
        task = input("Enter Task: ")
        tasks.append(task)
        print("Added a new Task!")
    elif choose == '2':
        if pin_enabled:
            if check_pin():
                print("\n Your Tasks: ")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}.{task}")
            else:
                print("WRONG PIN! Access denied...")
        else:
            print("\n Your Tasks: ")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}.{task}")   




    elif choose == '3':
        if not pin_enabled:
            pin = input("Enter a PIN to lock your tasks: ")
            pin_enabled = True
            print("Your Tasks are safe now!")
        else:
            if check_pin():
                pin_enabled = False
                pin = None
                print("Your Tasks are visibel without PIN...") 
        
        



    elif choose == '4':
        if pin_enabled and not check_pin():
            print("WRONG PIN! Access Denied!...")

        else:
            num = int(input("Enter the task no. : "))
            if 1 <= num <= len(tasks):
                tasks.pop(num - 1)
                print("Task is successfully deleted!")
            else:
                print("Invalid number... Try again...")
    elif choose == '5':
        print("See you later!")
        break

    else:
        print("Invalid option...Please Try again...")


