tasks=[]

while True:
    print("\n 1.Add task")
    print("2.View task")
    print("3.Delete task")
    print("4.Exit task")
    
    choice=input("Enter your choice:")

    if choice=="1":
        task=input("enter your task:")
        tasks.append(task)
        print("task added")
    elif choice=="2":
        if len(tasks)==0:
            print("No tasks to view")
        else:
            for i in range(len(tasks)):
                print(i+1,":",tasks[i])

    elif choice=="3":
        if len(tasks)==0:
            print("No tasks you delete")
        else:
            for i in range(len(tasks)):
                print(i+1,":",tasks[i])

            num=int(input("Enter a deleting number:"))
            
            if 1<= num <=len(tasks):
                removed=tasks.pop(num-1)
                print("Deleted:",removed)
            else:
                print("Invalid number")

    elif choice=="4":
        print("Existing tasks")
        break

    else:
        print("Invalid choice")



    
