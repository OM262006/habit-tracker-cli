import os

habits = {}

if os.path.exists("task.txt"):
    with open("task.txt","r") as file:
        for line in file:
            task, status = line.strip().split(",")
            habits[task] = True if status == "True" else False

while True:
    print("---------add todays task------------")
    print("1. add task")
    print("2. make task is done")
    print("3. view task")
    print("4. clg task")
    print("5. exit")

    choice = input("enter ur choice:" )

    if choice == "1":
        task = input("enter your task: ")
        habits[task] = False
        print("task is added")


    elif choice == "2":
        task = input("ennetr task name: ")

        if task in habits:
            habits[task] = True
            print("task is done")
        else:
            print("task not found")

    elif choice == "3":
        if not habits:
            print("no tasks yet")
        else:
            print("--------your tasks-------")
            for task, status in habits.items():
                if status:
                    print(task,"this task's are done")
                else:
                    print(task,"this task's are not done")

    elif choice == "4":

        print("------clg tasks------")
        print("1. assignment submission")
        print("2. lab submission")
        print("3. certificate submission")
        print("4. exit")

        clg_choice = input("enter ur choice: ")
        
        if clg_choice == "1":
            clg_task = input("enter which subject assignment: ")
            print("--------last date of assignment submission-------")
            Date = input("enter date: ")
            Month = input("enter month: ")
            Year = input("enter year")
            formatted_task = f"{clg_task} (Due: {Date}/{Month}/{Year})"
            habits[clg_task] = False
            print("clg assignment task is added")

        elif clg_choice == "2":
            clg_task = input("enter which lab: ")
            print("--------last date of lab submission-------")
            Date = input("enter date: ")
            Month = input("enter month: ")
            Year = input("enter year: ")
            formatted_task = f"{clg_task} (Due: {Date}/{Month}/{Year})"
            habits[clg_task] = False
            print("clg lab task is added")

        elif clg_choice == "3":
            
            cclg_task = input("enter which certificate: ")
            print("--------last date of certificate submission-------")
            Date = input("enter date: ")
            Month = input("enter month: ")
            Year = input("enter year: ")
            formatted_task = f"{clg_task} (Due: {Date}/{Month}/{Year})"
            habits[clg_task] = False
            print("clg lab task is added")

        elif clg_choice == "4":
            print("exiting...")

        else:
            print("enter valid choice...")

    
    elif choice == "5":
        with open("task.txt", "w") as file:
            for task, status in habits.items():
                file.write(f"{task},{status}\n")

        print("Saved & exiting 👋")
        break
        

    else:
        print("invalid choice")












       


