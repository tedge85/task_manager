# Notes: 
# 1. Use the following username and password to access the admin rights 
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the 
# program will look in your root directory for the text files.

#=====importing libraries===========
from calendar import c
import os 
from datetime import datetime, date
DATETIME_STRING_FORMAT = "%Y-%m-%d"
from dateutil.parser import parse
import datetime

# set variable for current date
current_DT = datetime.datetime.now()

# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]

# Create task list (list of dictionaries to store tasks for each user)
task_list = []
for t_str in task_data:
    curr_t = {}

    # Split by semicolon and manually add each component
    task_components = t_str.split(";")
    curr_t['username'] = task_components[0]
    curr_t['title'] = task_components[1]
    curr_t['description'] = task_components[2]
    curr_t['due_date'] = datetime.datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
    curr_t['assigned_date'] = datetime.datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
    curr_t['completed'] = True if task_components[5] == "Yes" else False

    task_list.append(curr_t)

#=====functions=====#

# Function registering a new user, asking for username, password, then confirmation of password
def reg_user(new_username, new_password, confirm_password):
    # Check if the new password and confirmed password are the same.
    # - Check if the new password and confirmed password are the same.
        if new_password == confirm_password:
            # - If they are the same, add them to the user.txt file,
            print("New user added")
            username_password[new_username] = new_password
            
            user_data = []
            
            with open("user.txt", "r") as out_file_read:
                # check if username exists
                for user in out_file_read:
                    # - If username exists, prompt to choose alternative
                    if new_username in user:
                        print("This username has already been registered. Please choose a different username.")
                # Otherwise add username and present a relevant message.
                else:
                    with open("user.txt", "w") as out_file:
                        for k in username_password:
                            user_data.append(f"{k};{username_password[k]}")
                        out_file.write("\n".join(user_data))

        # Otherwise you present a relevant message.
        else:
            return("Passwords do no match")

# Function that adds tasks
def add_task(task_username, task_title, task_description):
#'''Allow a user to add a new task to task.txt file
            #Prompt a user for the following: 
             #- A username of the person whom the task is assigned to,
             #- A title of a task,
             #- A description of the task and 
             #- the due date of the task.'''
        if task_username not in username_password.keys():
            print("User does not exist. Please enter a valid username")
            
        
        while True:
            try:
                task_due_date = input("Due date of task (YYYY-MM-DD): ")
                due_date_time = datetime.datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
                break

            except ValueError:
                print("Invalid datetime format. Please use the format specified")

        # Then get the current date.
        curr_date = date.today() ;''' Add the data to the file task.txt and Include 'No' to indicate if the task is complete.'''
        new_task = {
            "username": task_username,
            "title": task_title,
            "description": task_description,
            "due_date": due_date_time,
            "assigned_date": curr_date,
            "completed": False
        }

        task_list.append(new_task)
        with open("tasks.txt", "w") as task_file:
            task_list_to_write = []
            for t in task_list:
                str_attrs = [
                    t['username'],
                    t['title'],
                    t['description'],
                    t['due_date'].strftime(DATETIME_STRING_FORMAT),
                    t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                    "Yes" if t['completed'] else "No"
                ]
                task_list_to_write.append(";".join(str_attrs))
            task_file.write("\n".join(task_list_to_write))
        print("Task successfully added.")

# Function to display tasks assigned to all users
def view_all(array): 
# Reads the task from task.txt file and prints to the console in the 
# format of Output 2 presented in the task pdf (i.e. includes spacing
# and labelling) 
 
    for t in array:
        disp_str = f"Task: \t\t {array.index(t) + 1}) {t['title']}\n"
        disp_str += f"Assigned to: \t {t['username']}\n"
        disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Task Description: {t['description']}\n"
        disp_str += f"Task status: \t {'COMPLETE' if t['completed'] == True else 'INCOMPLETE'}\n"
        print(disp_str)

# Function to display user's assigned tasks
def view_mine(array):
    '''Reads the task from task.txt file and prints to the console in the 
    format of Output 2 presented in the task pdf (i.e. includes spacing
     and labelling)'''

    task_status = ""

    for t in array:
            if t['username'] == curr_user:
                disp_str = f"Task: \t\t {array.index(t) + 1}) {t['title']}\n"
                disp_str += f"Assigned to: \t {t['username']}\n"
                disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
                disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n" 
                disp_str += f"Task Description: {t['description']}\n"
                disp_str += f"Task status: \t {'COMPLETE' if t['completed'] == True else 'INCOMPLETE'}\n"
                print(disp_str)                
    
    task_num = input("Type a task number or type -1 to return to the main menu: ")
    
    if task_num.isdigit() == False:
        print("You have made a wrong choice. Please try again.")
        task_num = input("Type a task number or type -1 to return to the main menu: ")
    # Action if -1 chosen 
    elif int(task_num) == int(-1):
        return menu
    # Action if valid task number chosen
    elif array[int(task_num) -1]:
        curr_task_index = task_num -1
        task_status = input("Type 'complete' or 'edit': ")
    # Action if invalid task number chosen
    else:
        print("This task nunmber does not exist")
        task_num


    # actions if 'complete' chosen
    if task_status == "complete":
        array[curr_task_index]['completed'] = "Yes"
        print(f"\n \n*****Task status updated*****")
        disp_str = f"\nTask: \t\t {array[curr_task_index]['title']}\n"
        disp_str += f"Assigned to: \t {array[curr_task_index]['username']}\n"
        disp_str += f"Date Assigned: \t {array[curr_task_index]['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Due Date: \t {array[curr_task_index]['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Task Description: {array[curr_task_index]['description']}\n"
        disp_str += f"Task status: \t {'COMPLETE' if array[curr_task_index]['completed'] == 'Yes' else 'INCOMPLETE'}\n"
        print(disp_str)
        
        # Write result to task.txt file:
        with open("tasks.txt", "w") as task_file:
                task_list_to_write = []
                for t in task_list:
                    str_attrs = [
                        t['username'],
                        t['title'],
                        t['description'],
                        t['due_date'].strftime(DATETIME_STRING_FORMAT),
                        t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                        "Yes" if t['completed'] else "No"
                    ]
                    task_list_to_write.append(";".join(str_attrs))
                task_file.write("\n".join(task_list_to_write))

    # Action if 'edit' chosen
    elif task_status == "edit" and array[curr_task_index]['completed'] != 'Yes' :
        edit_choice = input("Type 'username' or 'due date' to edit username or due date: ")
        
        # Action if 'username' selected
        if edit_choice == "username":
            new_username = input("Type a new username: ")
            array[curr_task_index]['username'] = new_username 
            print(f"\n \n*****Task status updated*****")
            disp_str = f"\nTask: \t\t {array[curr_task_index]['title']}\n"
            disp_str += f"Assigned to: \t {array[curr_task_index]['username']}\n"
            disp_str += f"Date Assigned: \t {array[curr_task_index]['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Due Date: \t {array[curr_task_index]['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Task Description: {array[curr_task_index]['description']}\n"
            disp_str += f"Task status: \t {'COMPLETE' if array[curr_task_index]['completed'] == 'Yes' else 'INCOMPLETE'}\n"
            print(disp_str)
            
            # Write changes to text file
            with open("tasks.txt", "w") as task_file:
                task_list_to_write = []
                for t in task_list:
                    str_attrs = [
                        t['username'],
                        t['title'],
                        t['description'],
                        t['due_date'].strftime(DATETIME_STRING_FORMAT),
                        t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                        "Yes" if t['completed'] else "No"
                    ]
                    task_list_to_write.append(";".join(str_attrs))
                task_file.write("\n".join(task_list_to_write))

        # Action if 'due date' chosen
        elif edit_choice == "due date":
            try:
                new_due_date = input("Type a new due date (YYYY-MM-DD): ")
                new_due_date = datetime.datetime.strptime(new_due_date, DATETIME_STRING_FORMAT)
            except ValueError:
                print("Invalid datetime format. Please use the format specified.")

            
            array[curr_task_index]['due_date'] = new_due_date 
            print(f"\n \n*****Task status updated*****")
            disp_str = f"\nTask: \t\t {array[curr_task_index]['title']}\n"
            disp_str += f"Assigned to: \t {array[curr_task_index]['username']}\n"
            disp_str += f"Date Assigned: \t {array[curr_task_index]['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Due Date: \t {array[curr_task_index]['due_date']}\n" #########take out time #########fix errors for nums chosen earlier in menu
            disp_str += f"Task Description: {array[curr_task_index]['description']}\n"
            disp_str += f"Task status: \t {'COMPLETE' if array[curr_task_index]['completed'] == 'Yes' else 'INCOMPLETE'}\n"
            print(disp_str)
            # Write changes to text file
            
            with open("tasks.txt", "w") as task_file:
                task_list_to_write = []
                for t in task_list:
                    str_attrs = [
                        t['username'],
                        t['title'],
                        t['description'],
                        t['due_date'].strftime(DATETIME_STRING_FORMAT),
                        t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                        "Yes" if t['completed'] else "No"
                    ]
                    task_list_to_write.append(";".join(str_attrs))
                task_file.write("\n".join(task_list_to_write))
            

            # Condition if neither value typed
        else:
             print("Please select a valid option.")
             task_num 
    '''function that displays report of total number of tasks,
    completed tasks, uncompleted tasks, tasks overdue, and percentages
    of incomplete and overview tasks, respectively
    '''
# function to generate text files for user and task information: task_overview.txt & user_overview.txt
def generate_report(task_data):
    # Task overview
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    for t in task_data:
        if t["completed"] == True: 
            b += 1
        elif parse(str(t['due_date'])) < current_DT:
            d += 1
            c += 1
        else:
            c += 1
            e += 1
        a += 1
    
    task_stats = [   
        'total', a,
        'completed tasks', b,
        'uncompleted tasks', c,
        'uncompleted and overdue tasks', d,
        'percentage of tasks that are incomplete', f'{round(c / a * 100)}%',
        'percentage of tasks that are overdue', f'{round(d / a * 100)}%'
    ]

    # Convert task_stats dictionary to string
    #task_stats_str = '\n'.join(task_stats)

    # User overview
    usernames = [d["username"] for d in task_data]
    unique_usernames = []
    for name in usernames:
        if name not in unique_usernames:
            unique_usernames.append(name)

    users_registered = len(unique_usernames)
    task_total = a

    user_tasks = [t["title"] for t in task_data if t["username"] == curr_user]
    user_tasks_total = len(user_tasks)
    user_task_percentage = round(user_tasks_total / a * 100)
    user_completed_tasks_percentage = round(len([d for d in task_data if d["completed"] == True and d["username"] == curr_user]) / user_tasks_total * 100)
    user_uncompleted_tasks_percentage = round(len([d for d in task_data if d["completed"] == False and d["username"] == curr_user]) / user_tasks_total * 100)
    user_incompleted_overdue_tasks_percentage = round(len([d for d in task_data if d["completed"] == False and parse(str(d['due_date'])) < current_DT and d["username"] == curr_user]) / user_tasks_total * 100)
    
    user_stats = [
        "total number of users registered", users_registered,
        "total number of tasks assigned", task_total,
        "user", curr_user,
        "total number of tasks assigned to user", user_tasks_total,
        "percentage of total tasks assigned to user", f"{user_task_percentage}%",
        "percentage of user's tasks that have been completed", f"{user_completed_tasks_percentage}%",
        "percentage of user's tasks that have not been completed", f"{user_uncompleted_tasks_percentage}%",
        "percentage of user's tasks that have not been completed and are overdue", f"{user_incompleted_overdue_tasks_percentage}%"
    ]
    # Convert user_stats dictionary to string
    user_stats_str = ";".join(str(s) for s in user_stats)
    
    task_stats_str = ";".join(str(s) for s in task_stats)

    # Output data to user: *********need to change***************
    print(f"\n******TASK OVERVIEW AND USER OVERVIEW REPORTS GENERATED******\n")
    
    # Write results to task_overview.txt file:
    with open("task_overview.txt", "w+") as t_o_file:
        t_o_file.write(task_stats_str)

    # Write results to user_overview.txt file:
    with open("user_overview.txt", "w+") as u_o_file:
        u_o_file.write(user_stats_str)

# Function that reads task_overview.txt and user_overview.txt and displays contents to user
def display_stats(tasks_file,user_file):
    '''If the user is an admin they can display statistics about number of users
            and tasks.'''
    # Create task_overview.txt and user_overview.txt if it doesn't exist (as generate_report function not yet called)
    if not os.path.exists("task_overview.txt") and not os.path.exists("user_overview.txt"):
        generate_report(task_list)

    with open(tasks_file, 'r') as t_o_file:
        task_overview = t_o_file.read().split(";")

    with open(user_file, 'r') as u_o_file:
        user_overview = u_o_file.read().split(";")

    
    print("-----------------------------------")
    print("******TASK OVERVIEW******")
    print(f"{task_overview[0]}:\t\t\t\t\t\t\t\t\t\t{task_overview[1]}")
    print(f"{task_overview[2]}:\t\t\t\t\t\t\t\t{task_overview[3]}")
    print(f"{task_overview[4]}:\t\t\t\t\t\t\t\t{task_overview[5]}")
    print(f"{task_overview[6]}:\t\t\t\t\t\t\t{task_overview[7]}")
    print(f"{task_overview[8]}:\t\t\t\t\t{task_overview[9]}")
    print(f"{task_overview[10]}:\t\t\t\t\t\t{task_overview[11]}")
    print("\n******USER OVERVIEW******")
    print(f"{user_overview[0]}:\t\t\t\t\t\t{user_overview[1]}")
    print(f"{user_overview[2]}:\t\t\t\t\t\t\t{user_overview[3]}")
    print(f"\n{user_overview[4]}:\t\t\t\t\t\t\t\t\t\t{user_overview[5]}")
    print(f"{user_overview[6]}:\t\t\t\t\t\t{user_overview[7]}")
    print(f"{user_overview[8]}:\t\t\t\t\t{user_overview[9]}")
    print(f"{user_overview[10]}:\t\t\t\t{user_overview[11]}")
    print(f"{user_overview[12]}:\t\t\t{user_overview[13]}")
    print(f"{user_overview[14]}:\t{user_overview[15]}")        
    print("-----------------------------------")

#====Login Section====
'''This code reads usernames and password from the user.txt file to 
    allow a user to login.
'''
# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

logged_in = False
while not logged_in:

    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password.keys():
        print("User does not exist")
        continue
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
        continue
    else:
        print("Login Successful!")
        logged_in = True


while True:
    # presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    print()
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
gr - Generate reports
ds - Display statistics
e - Exit
: ''').lower()

    if menu == 'r':
       reg_user(input("New Username: "), input("New Password: "), input("Confirm Password: "))

    elif menu == 'a':
        add_task(input("Name of person assigned to task: "), input("Title of Task: "), input("Description of Task: "))
                
    elif menu == 'va':
        view_all(task_list)
                    
    elif menu == 'vm':
        view_mine(task_list)      
    
    elif menu == "gr":
        generate_report(task_list)

    elif menu == 'ds' and curr_user == 'admin': 
        display_stats("task_overview.txt","user_overview.txt")    

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")

