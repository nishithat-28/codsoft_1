print("----------TO DO LIST----------\n\n")
tdlist=[]
while True:
    print("Operations:")
    print("1) Create Task\n2) Delete Task\n3) Update Task\n4) Display Tasks\n5) Exit")
    ch=int(input("Choose Operation = "))
    if ch==1:
        tdlist.append(input("New task name: "))
        print("New task added.\n")
    elif ch==2:
        try:
            n1=int(input("Task number to be deleted: "))
            tdlist.pop(n1-1)
        except:
            print("Task not present!\n")
        else:
            print("Task deleted.\n")
    elif ch==3:
        if len(tdlist)==0:
            print("Your to do list is empty!")
        else:
            try:
                n2=int(input("Task number to be updated: "))
                ut=input("Task name: ")
                tdlist[n2-1]=ut
            except:
                print("Task not present!\n")
            else:
                print("Task updated.\n")
    elif ch==4:
        if len(tdlist)==0:
            print("Your to do list is empty!\n")
        else:
            print("-----------------------------")
            print("          Your List          ")
            for i in range(len(tdlist)):
                print("{}) {}".format(i+1,tdlist[i]))
            print("-----------------------------\n")
    elif ch==5:
        break
    else:
        print("Invalid choice!\n")
