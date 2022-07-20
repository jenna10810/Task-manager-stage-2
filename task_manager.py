#===== Importing libraries===========
import datetime
from collections import Counter


username = ""
task= ""

# =========Functions=========== 

# Function to display the menu options
def menu_options():

    menu = input('''Select one of the following Options below:
        r  - \tRegistering a user
        a - \tAdding a task
        va - \tView all tasks
        vm - \tview my task
        e - \tExit
        \t\t: ''').lower()
    
    if menu == "r":
        reg_user()

    elif menu == "a":
        add_task()

    elif menu == "va":
        view_all()

    elif menu == "vm":
        view_mine()

# =========== Function to read all tasks ===========
def read_all_tasks():
    task_list = []

    # Open the file 'tasks.tx' and read all of the lines
    with open("tasks.txt" , "r") as task_file:
        for line in task_file.readlines():
            columns = line.strip().split(", ") 
            task_list.append({
                "task_number": columns[0],
                "name": columns[2],
                "description": columns[3],
                "date_assigned": columns[4],
                "assigned_to": columns[1],
                "due_date": columns[5],
                "completed": columns[-1]
            })     
    return task_list

# =========== Prints a task in a user friendly manner ===========
def print_task (task): 
    print("%-20s %s" % ("Task number", task["task_number"]))
    print("%-20s %s" % ("Task", task["name"]))
    print("%-20s %s" % ("Assigned to", task["assigned_to"]))
    print("%-20s %s" % ("Date assigned", task["date_assigned"]))
    print("%-20s %s" % ("Due date", task["due_date"]))
    print("%-20s %s" % ("Task complete?", task["completed"]))
    print("%-20s %s" % ("Task description:", "\n" + task["description"] + "\n"))

# =========== Function to register a new user ===========
def reg_user():
    if username == "admin":
            print("You have chosen to register a new user:")
            # Here the admin can add the new user's details
            new_username = input("Enter your username: \t\t")
            if new_username in usernames_login:
                new_username = input("You have entered an existing username, please enter another username:\t")
            new_password = input("Enter your password: \t\t")
            password_validation = input("Please confirm your password:\t")
        
        # Validate the user's new password against the one they enetered first, if it does not match, they have to try again
            while new_password != password_validation:
                new_password = input("Please enter the same password: ")
                password_validation = input("Please confirm your password:\t")

            # Add the new user's data to the file 'user.txt'
            with open("user.txt" , "a") as username_file:
                username_file.write("\n" + new_username + ", " + new_password)
    else: 
        print("You are not allowed to add new users \n")

# =========== Function to add tasks to the file 'tasks.txt' ===========
def add_task():
    # Promp the user to enter new task details to the 'task.txt' file
        username_assigned_to = input("To who is this task assigned to? \t")
        title_of_task = input("What is the title of the task? \t\t")
        description_of_task = input("Describe the task: \t\t\t")
        due_date_of_task = input("When is this task due? (DD Month Year)\t")
        today_date = datetime.datetime.today()
        task_completed = "No"

        # Task counter from https://stackoverflow.com/questions/67332033/python-how-to-correctly-increment-this-for-loop-with-a-counter-variable
        with open("tasks.txt" , "r") as task_file:
            for lines in task_file:
                lines = [line.strip("\n").strip(" ").split(", ") for line in task_file]
                last_line = lines[-1]
                task_number = int(last_line[0])
                task_number += 1
    
        # Add the user's input to the 'task.txt' file
        with open("tasks.txt" , "a") as task_file:
            task_file.write(f"\n{task_number}, {username_assigned_to}, {title_of_task}, {description_of_task}, {due_date_of_task}, {today_date}, {task_completed}" )

# =========== Function to view all of the tasks in the file 'tasks.txt' ===========
def view_all():
    # Declare new lists where the corresponding information will be listed
        task_list = read_all_tasks()
    
        # Use a for loop to run through all of the lines and print out the tasks in an easy to raed format
        for task in task_list:
            print_task(task)

# =========== Function that updates the 'tasks.txt' file ===========
def update_tasks_file(tasks):
# tasks will potentially be updated
    with open("tasks.txt" , 'w') as task_file:
        for task in tasks:
            line = task["task_number"] + ", " +  task["assigned_to"]+ ", " + task["name"]+ ", " + task["description"]+ ", " + task["date_assigned"]+ ", " + task["due_date"]+ ", " +task["completed"] + '\n'
            task_file.write(line)

# =========== Function to view the logged in user's tasks ===========
def view_mine():
    list_tasks = read_all_tasks()   # Call the function 'read_all_tasks'
    users_tasks = []                # Create an empty list to store the tasks in
    for task in list_tasks:
        if task["assigned_to"] == username:   
            users_tasks.append(task)    # Append the user's tasks to the 'user_tasks' list
            print_task(task)            # Print out the user's tasks

    task_selection = input("Enter a task number to view it, or enter '-1' to go back to the main menu:\t") # find thetask with that number and print it
    if task_selection == -1:
        return menu_options()
    else:
        # Find the user's task with the specified number
        specified_task = None
        for task in users_tasks:
            if task["task_number"] == task_selection:
                specified_task = task
                break
        if specified_task == None:
            print("Invalid taks number specefied. Exiting")
            return menu_options()
        # Print and mark the correct task
        print_task(specified_task)
        mark_task(specified_task)
        update_tasks_file(list_tasks)

# =========== Function to diplay the admin's menu options ===========
def admin_menu_options():
    admin_menu = input('''Select one of the following options below:
        r  - \tRegistering a user
        a - \tAdding a task
        va - \tView all tasks
        vm - \tview my task
        gr - \tGenerate reports
        ds - \tDisplay ststistics
        e - \tExit
        \t\t: ''').lower()
    
    if admin_menu == "r":
        reg_user()
    elif admin_menu == "a":
        print(add_task())
    elif admin_menu == "va":
        view_all()
    elif admin_menu == "vm":
        view_mine()
    elif admin_menu == "gr":
        generate_reports()
    elif admin_menu == "ds":
        display_stats()

# =========== Function to generate the reports for the admin ===========
def generate_reports():
    # =================== TASK OVERVIEW ========================================

    # Total number of tasks that have been tracked
    # Total number of completed tasks
    # The total number of uncompleted tasks
    count_yes = 0
    count_no = 0

    with open("task_overview.txt" , "w") as task_overview_file:
        
        for task in read_all_tasks():
            if task["completed"] == "Yes":
                count_yes = count_yes + 1
            elif task["completed"] == "No":
                count_no = count_no + 1

        task_overview_file.write(f"Total amount of tasks assigned: {count_yes + count_no}\n")
        task_overview_file.write(f"\nTasks completed: \t{count_yes}\nUncompleted tasks: \t{count_no}\n")   

        # Total tasks not complteted and overdue
        now = datetime.datetime.now()
        overdue_tasks_counter = 0
        for task in read_all_tasks():
            task_due_date = datetime.datetime.strptime(task["due_date"], "%d %b %Y")
            if  task["completed"] == "No" and task_due_date < now:
                overdue_tasks_counter += 1

        task_overview_file.write(f"\nOverdue tasks:\t\t{overdue_tasks_counter} \n")

        # Percentage of tasks that are incomplete
        percentage_uncompleted_tasks = count_no / (count_yes + count_no) * 100
        task_overview_file.write(f"\n% Incomplete tasks:\t\t{percentage_uncompleted_tasks}%\n")

        # Percentage of tasks that are overdue
        task_overview_file.write(f"% Overdue tasks:\t\t{overdue_tasks_counter / (count_yes + count_no) * 100} %")
    # ==================== User Overview ========================================
    
    with open("user_overview.txt", "w") as user_overview_file:
        all_tasks = read_all_tasks()
        amount_of_tasks = len(all_tasks)
        # TODO Total number of users registered in user.txt

        # Total number of tasks that have been generated
        user_overview_file.write(f"Total number of tasks: {amount_of_tasks} \n\n")

        # For each user: total number of tasks assigned to them
        now = datetime.datetime.today()
        user_tasks = {}
        for task in all_tasks:
            tasks_user = task["assigned_to"]
            task_is_overdue = task["completed"] == "No" and datetime.datetime.strptime(task["due_date"], "%d %b %Y") < now
            if tasks_user not in user_tasks:
                user_tasks[tasks_user] = {
                    "completed": 1 if task["completed"] == "Yes" else  0,
                    "overdue": 1 if task_is_overdue else 0,
                    "total_tasks": 1
                }
            else:
                user_tasks[tasks_user] = {
                    "completed": user_tasks[tasks_user]["completed"] + 1 if task["completed"] == "Yes" else  user_tasks[tasks_user]["completed"],
                    "overdue":  user_tasks[tasks_user]["overdue"] + 1 if task_is_overdue else user_tasks[tasks_user]["overdue"],
                    "total_tasks": user_tasks[tasks_user]["total_tasks"] + 1
                }

        user_overview_file.write("Tasks assigned:\n")
        for name in user_tasks.keys():
            users_summary = user_tasks[name]
            user_overview_file.write(name + ":\t\t\t\t" + str(users_summary["total_tasks"]) + "\n")

    
        # For each user: percentage of total tasks have been assigned to the user
        user_overview_file.write("\nPercentage of tasks assigned to user:\n")
        for name in user_tasks.keys():
            users_summary = user_tasks[name]
            user_overview_file.write(name + ":\t\t\t\t" + str(users_summary["total_tasks"]/ amount_of_tasks * 100) + "\n")


        # For each user: percentage of tasks assigned have been completed
        user_overview_file.write("\nPercentage of assigned completed tasks:\n")
        for name in user_tasks.keys():
            users_summary = user_tasks[name]
            user_overview_file.write(name + ":\t\t\t\t" + str(users_summary["completed"] / users_summary["total_tasks"] * 100) + "\n")

        # For each user: percentage of tasks assigned must still be completed
        user_overview_file.write("\nPercentage of assigned completed tasks:\n")
        for name in user_tasks.keys():
            users_summary = user_tasks[name]
            users_incomplete_tasks_amount = users_summary["total_tasks"] - users_summary["completed"]
            user_overview_file.write(name + ":\t\t\t\t" + str(users_incomplete_tasks_amount / users_summary["total_tasks"] * 100) + "\n")

        # For each user: percentage of tasks assigned that are incomplete and overdue
        user_overview_file.write("\nPercentage of assigned incomplete and overdue tasks:\n")
        for name in user_tasks.keys():
            users_summary = user_tasks[name]
            user_overview_file.write(name + ":\t\t\t\t" + str(users_summary["overdue"] / users_summary["total_tasks"] * 100) + "\n")
#  =============================================


# ===========Function to display the statistics for the admin ===========             
def display_stats():
     # Open the file, 'tasks.txt' 
            with open("tasks.txt" , "r") as task_file:
                count = Counter(line.split(", ")[1] for line in task_file)  # Count the amount of times a task is assigned to a user - 
                                                                            # I got this Counter from doing task 20
            print("Tasks assigned:")
            for key, value, in count.items():
                print(key + ":\t" + str(value))
                    
                    
            list_of_names_and_tasks = []    # Create an empty list 
            dict_of_names_and_tasks = {}    # Create an empty dictionary
            with open("tasks.txt" , "r") as task_file:
                for lines in task_file:
                    columns = lines.split(", ")      # Split the line by the commas in order to use the data
                    list_of_names_and_tasks.append(columns[1])      # Only add the user's name to the list
                    dict_of_names_and_tasks = (Counter(list_of_names_and_tasks))    # Count the amount of tasks assigned to a user

            for key, value in dict_of_names_and_tasks.items():
                print(f"\nUser:\t{key}\nTasks:\t{value}")    # Print out the username and amount of tasks

# =========== Function to mark the task completed ===========
def mark_task(task):
    if task["completed"] == "No":
        edit_options = input('''What would you like to edit this task?
                                mt:\t mark task as completed:\t
                                u:\t username to who the task is assigned to:\t
                                dd:\t the due date of the task:\t
                                no:\t I don't want to edit this task\t
                                :\t''')
        
        if edit_options == "u":
            task["assigned_to"] = input("Who is the task assigned to now?\t")
        elif edit_options == "dd":
            task["due_date"] = input("What is the new due date of the task\t")
        elif edit_options == "mt":
            task["completed"] = "Yes"
        elif edit_options == "no":
            menu_options()

        
#====Login Section====
# Create new lists to store the 'user.txt' passwords and usernames
usernames_login = []
passwords_login = []


# Open the file 'user.txt' and create a list of the authorised passwords and usernames
with open ("user.txt" , "r") as f:
    for lines in f.readlines():
        columns = lines.strip().split(", ")
        usernames_login.append(columns[0])
        passwords_login.append(columns[-1])

# Validate the user's login details against the details found in the file user.txt
login = False

while login == False:
    username = input("Enter your username: \t")
    password = input("Enter your password: \t")   

    # If the username is not in the list, but the password is, then the user must try again
    if (username not in usernames_login) and (password in passwords_login):
        print("Wrong username, please try again:")
        continue    # This allows the user to try agian by going to the top again and asking them for their login details
    # If the username is in the list, but the password is not, then the user must try again
    elif (username in usernames_login) and (password not in passwords_login):
        print("Wrong password, please try again:")
        continue
    elif (username not in usernames_login) and (password not in passwords_login):
        print("Wrong username and password, please try again:")
        continue
    else: 
        break # The user's credentials are valid

if username == "admin":
    admin_menu_options()
else:
    menu_options()
