#------------------
# To-Do-List-code
#------------------

# this is just a code based app without any complications.

# there are no extra things used except python.

# It can run in any python console, we just need to copy and paste it anywhere you want.


# this code can also set a PIN.
# So that it can lock the tasks and visible only when it gets the correct PIN.

tasks = []
pin_enabled = False #this is because the lock should be off until it gets the PIN manually.
pin = None

def check_pin():
    entered = input("Enter PIN: ")
    return entered == pin

# Used funtions here, so that, It can be used anywhere.

while True:
    print("\n To-Do-List App")
    
    
    options= ["Add tasks", "Inspect Tasks", "Lock/unlock Your tasks", "Delete tasks", "Quit"]

    for n, option in enumerate(options, start=1):
        print(f"{n}.{option}")

# Used enumerate to number the options automatically without any struggles in further updates.


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

# that function is used here


    elif choose == '3':
        if not pin_enabled:
            pin = input("Enter a PIN to lock your tasks: ")
            pin_enabled = True
            print("Your Tasks are safe now!")
        else:
            if check_pin():
                pin_enabled = False
                pin = None
                print("Your Tasks are visible without PIN...") 
        
    # that function is also used here



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




