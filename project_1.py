# buildind a to do list

def take_task():
    print("WELCOME TO YOUR CUSTOM TO_DO LIST TRACKER, HERE YOU CAN LIST YOUR TASKS ACCORDING TO YOUR PRIORITIES")
    to_do_list = []

    top_priority =[]
    medium_priority =[]
    low_priority =[]

    while True:
        priority = input("first tell me the task you will enter has what level of priority, top/medium/low: ").lower()
        task = input("now enter your task : ")

        if priority == "top":
            top_priority.append(task)
        elif priority == "medium":
            medium_priority.append(task)
        elif priority == "low":
            low_priority.append(task)

        

        ans = input("do you want to list some more tasks, (enter yes or no): ")

        if ans == "no":
            break

    to_do_list.append(top_priority)
    to_do_list.append(medium_priority)
    to_do_list.append(low_priority)

    print("your to do list is as follows: ")
    for i in to_do_list:
        for j in i:
            print(j)

 # this function will manage the list by removing the task which you have completed and want to remove from the list, you can remove as many tasks as you want until you say no to the question which will be asked after every task removal   
def task_maneger(to_do_list):
    
    while True
        task_to_remove = input("enter the task you want to remove : ")

        for list in to_do_list:
            if task_to_remove in list:
                list.remove(task_to_remove)
                print(f"{task_to_remove} has been removed from your to do list")
                break
    
        remove_task = input("do you want to remove any other task from the list which you have entered, (enter yes or no): ")
        if remove_task == "no":
            break

take_task()

ask = input("do you want to manage your task list, (enter yes or no): ").lower()

if ask == "yes":
    task_maneger(to_do_list)

print("your revised to do list is as follows: ")
    
        