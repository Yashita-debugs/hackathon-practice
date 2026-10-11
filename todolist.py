tasks=[]
def add_task():
    description =input("enter the task: ")
    priority=input("enter the priority as low or high: ")
    group=input("enter the group name: ")

    task={"description":description,"priority":priority,"group":group}
    tasks.append(task) 

def view_tasks():
    if len(tasks)==0:
        print("There are no current tasks")
    else:
        for i, task in enumerate(tasks,start=1):
            print(i,".",task["description"])
            print("Priority: ",task["priority"])
            print("Group: ",task["group"])

def remove_tasks():
    if len(tasks)==0:
        print("There are no tasks to delete")

    else:    
        print("Choose the task number you want removed")
        view_tasks()
        try:
            n=int(input("Enter the task number you want delete: "))
        except ValueError:
            print("Please enter a number and not letters or special characters.")
            return
        if n<=0 or n>len(tasks):
            print("Invalid index entered")
        else:
            removed=tasks.pop(n-1) 
            print("Removed task: ",removed["description"])
def main():
    while True:
        print("Main Menu")
        print("\n 1. Add a task \n 2. Delete a task \n 3. Show all task \n 4. Quit the to-do list")
        try:
            ch = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Please type a number, not letter or special characters.")
            continue
        if ch==1:
            add_task()
        elif ch==2:
            remove_tasks()
        elif ch==3:
            view_tasks()
        elif ch==4:
            break
        else:
            print("invalid choice entered")
        
main()

