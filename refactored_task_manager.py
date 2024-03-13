from calendar import c
import os
from datetime import datetime, date
DATETIME_STRING_FORMAT = "%Y-%m-%d"
from dateutil.parser import parse
import datetime
            
class Task:
    task_list = []
    current_DT = datetime.datetime.now()

    def __init__(self, txt_file):
        self.txt_file = txt_file
           
        # Create the .txt file if it doesn't exist 
        if not os.path.exists(txt_file):
            with open(txt_file, "w") as default_file:
                pass
        
        # Read the date in .txt file then store the 
        # data in a dictionary, ready to access by program.
        # Create tasks.txt if it doesn't exist
        with open(txt_file, 'r') as task_file:
            self.task_data = task_file.read().split("\n")
            self.task_data = [t for t in self.task_data if t != ""]

            for t_str in self.task_data:
                curr_task = {}
                # Split by semicolon and manually add each component
                task_components = t_str.split(";")
                curr_task['username'] = task_components[0]
                curr_task['title'] = task_components[1]
                curr_task['description'] = task_components[2]
                curr_task['due_date'] = datetime.datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
                curr_task['assigned_date'] = datetime.datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
                curr_task['completed'] = True if task_components[5] == "Yes" else False

                # Save each user's task in an array of dictionaries
                self.task_list.append(curr_task)
        
    def write_to_txt_file(self, txt_file):
        with open(txt_file, "w") as task_file:
            task_list_to_write = []
            for t in self.task_list:
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

    def add_task(self, task_username, task_title, task_description):
        '''Allows a user to add a new task to task.txt file'''
            # Prompt a user for the following: 
             #- A username of the person whom the task is assigned to,
             #- A title of a task,
             #- A description of the task and 
             #- the due date of the task.'''
        if task_username not in user.username_password.keys():
            print("User does not exist. Please enter a valid username")
            
        
        while True:
            try:
                task_due_date = input("Due date of task (YYYY-MM-DD): ")
                due_date_time = datetime.datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
                break

            except ValueError:
                print("Invalid datetime format. Please use the format specified")

        # Then get the current date.
        curr_date = date.today() ;''' Add the data to the file task.txt and indicate whether or not the task is complete.'''
        new_task = {
            "username": task_username,
            "title": task_title,
            "description": task_description,
            "due_date": due_date_time,
            "assigned_date": curr_date,
            "completed": False
        }

        self.task_list.append(new_task)
        
        self.write_to_txt_file(self.txt_file)

    def generate_report(self, task_data):
        total_tasks = 0
        completed_tasks = 0
        uncompleted_tasks = 0
        uncompleted_overdue_tasks = 0
    
        for t in task_data:
            if t["completed"] == True: 
                completed_tasks += 1
            elif parse(str(t['due_date'])) < self.current_DT:
                uncompleted_overdue_tasks += 1
                uncompleted_tasks += 1
            else:
                completed_tasks += 1
            total_tasks += 1
    
        task_stats = [   
            'total', total_tasks,
            'completed tasks', completed_tasks,
            'uncompleted tasks', uncompleted_tasks,
            'uncompleted and overdue tasks', uncompleted_overdue_tasks,
            'percentage of tasks that are incomplete', f'{round(uncompleted_tasks / total_tasks * 100)}%',
            'percentage of tasks that are overdue', f'{round(uncompleted_overdue_tasks / total_tasks * 100)}%'
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

        user_tasks = [t["title"] for t in task_data if t["username"] == user.curr_user]
        user_tasks_total = len(user_tasks)
        user_task_percentage = round(user_tasks_total / total_tasks * 100)
        user_completed_tasks_percentage = round(len([d for d in task_data if d["completed"] == True and d["username"] == user.curr_user]) / user_tasks_total * 100)
        user_uncompleted_tasks_percentage = round(len([d for d in task_data if d["completed"] == False and d["username"] == user.curr_user]) / user_tasks_total * 100)
        user_incompleted_overdue_tasks_percentage = round(len([d for d in task_data if d["completed"] == False and parse(str(d['due_date'])) < self.current_DT and d["username"] == user.curr_user]) / user_tasks_total * 100)
    
        user_stats = [
            "total number of users registered", users_registered,
            "total number of tasks assigned", total_tasks,
            "user", user.curr_user,
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

    def display_stats(self, tasks_file, user_file):
        '''If the user is an admin they can display statistics about number of users
                and tasks.'''
        # Create tasks.txt if it doesn't exist
        if not os.path.exists("task_overview.txt") and not os.path.exists("user_overview.txt"):
            self.generate_report(self.task_list)

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

    def view_all(self, task_data): 
           '''Reads the task from .txt file and prints to the console in the 
              format of Output 2 presented in the task pdf (i.e. includes spacing
              and labelling)''' 
 
           for task in task_data:
                disp_str = f"Task: \t\t {task_data.index(task) + 1}) {task['title']}\n"
                disp_str += f"Assigned to: \t {task['username']}\n"
                disp_str += f"Date Assigned: \t {task['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
                disp_str += f"Due Date: \t {task['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
                disp_str += f"Task Description: {task['description']}\n"
                disp_str += f"Task status: \t {'COMPLETE' if task['completed'] else 'INCOMPLETE'}\n"
                print(disp_str)

    def view_mine(self, task_data):
        '''Reads user's own tasks from task.txt file and prints to the console'''

        task_status = ""

        for t in task_data:
                if t['username'] == user.curr_user:
                    disp_str = f"Task: \t\t {task_data.index(t) + 1}) {t['title']}\n"
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
        elif task_data[int(task_num) -1]:
            curr_task_index = int(task_num) -1
            task_status = input("Type 'complete' or 'edit': ")
        # Action if invalid task number chosen
        else:
            print("This task nunmber does not exist")
            task_num


        # Actions if 'complete' chosen
        if task_status == "complete":
            task_data[curr_task_index]['completed'] = "Yes"
            print(f"\n \n*****Task status updated*****")
            disp_str = f"\nTask: \t\t {task_data[curr_task_index]['title']}\n"
            disp_str += f"Assigned to: \t {task_data[curr_task_index]['username']}\n"
            disp_str += f"Date Assigned: \t {task_data[curr_task_index]['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Due Date: \t {task_data[curr_task_index]['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Task Description: {task_data[curr_task_index]['description']}\n"
            disp_str += f"Task status: \t {'COMPLETE' if task_data[curr_task_index]['completed'] == 'Yes' else 'INCOMPLETE'}\n"
            print(disp_str)
        
            # Write result to task.txt file:
            self.write_to_txt_file(self.txt_file)

        # Action if 'edit' chosen
        elif task_status == "edit" and task_data[curr_task_index]['completed'] != 'Yes' :
            edit_choice = input("Type 'username' or 'due date' to edit username or due date: ")
        
            # Action if 'username' selected
            if edit_choice == "username":
                new_username = input("Type a new username: ")
                task_data[curr_task_index]['username'] = new_username 
                print(f"\n \n*****Task status updated*****")
                disp_str = f"\nTask: \t\t {task_data[curr_task_index]['title']}\n"
                disp_str += f"Assigned to: \t {task_data[curr_task_index]['username']}\n"
                disp_str += f"Date Assigned: \t {task_data[curr_task_index]['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
                disp_str += f"Due Date: \t {task_data[curr_task_index]['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
                disp_str += f"Task Description: {task_data[curr_task_index]['description']}\n"
                disp_str += f"Task status: \t {'COMPLETE' if task_data[curr_task_index]['completed'] == 'Yes' else 'INCOMPLETE'}\n"
                print(disp_str)
           
                # Write changes to text file
                self.write_to_txt_file(self.txt_file)                                              

            # Action if 'due date' chosen
            elif edit_choice == "due date":
                try:
                    new_due_date = input("Type a new due date (YYYY-MM-DD): ")
                    new_due_date = datetime.datetime.strptime(new_due_date, DATETIME_STRING_FORMAT)
                except ValueError:
                    print("Invalid datetime format. Please use the format specified.")

            
                task_data[curr_task_index]['due_date'] = new_due_date 
                print(f"\n \n*****Task status updated*****")
                disp_str = f"\nTask: \t\t {task_data[curr_task_index]['title']}\n"
                disp_str += f"Assigned to: \t {task_data[curr_task_index]['username']}\n"
                disp_str += f"Date Assigned: \t {task_data[curr_task_index]['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
                disp_str += f"Due Date: \t {task_data[curr_task_index]['due_date']}\n" 
                disp_str += f"Task Description: {task_data[curr_task_index]['description']}\n"
                disp_str += f"Task status: \t {'COMPLETE' if task_data[curr_task_index]['completed'] == 'Yes' else 'INCOMPLETE'}\n"
                print(disp_str)
                
                # Write changes to text file
                write_to_txt_file(self.txt_file)
            

                # Condition if neither value typed
            else:
                 print("Please select a valid option.")

class User():
    username_password = {}
    user_data = []

    def __init__(self, user_txt_file):
        self.user_txt_file = user_txt_file  

        '''This code reads usernames and password from the user.txt file to 
        allow a user to login.'''

        # If no user.txt file, write one with a default admin account
        if not os.path.exists(user_txt_file):
            with open(user_txt_file, "w") as default_file:
                default_file.write("admin;password")

        # Read in user_data
        with open(user_txt_file, 'r') as user_file:
            user_data = user_file.read().split("\n")

        # Convert to a dictionary
        for user in user_data:
            username, password = user.split(';')
            self.username_password[username] = password

        logged_in = False
        while not logged_in:

            print("LOGIN")
            self.curr_user = input("Username: ")
            self.curr_pass = input("Password: ")
            if self.curr_user not in self.username_password.keys():
                print("User does not exist")
                continue
            elif self.username_password[self.curr_user] != self.curr_pass:
                print("Wrong password")
                continue
            else:
                print("Login Successful!")
                logged_in = True
        

    
    def reg_user(self, new_username, new_password, confirm_password):
        '''Registers a new user, asking for username, password, then confirmation of password'''
        # Checks if the new password and confirmed passwords are the same.
        if new_password == confirm_password:
                
                print("New user added")
                self.username_password[new_username] = new_password
            
                
            
                with open("user.txt", "r") as out_file_read:
                    
                    for user in out_file_read:
                        # If username exists, prompt to choose alternative
                        if new_username in user:
                            print("This username has already been registered. Please choose a different username.")
                    # Otherwise add username and present a relevant message.
                    else:
                        with open("user.txt", "w") as out_file:
                            for k in self.username_password:
                                self.user_data.append(f"{k};{self.username_password[k]}")
                            out_file.write("\n".join(self.user_data))

        # Otherwise you present a relevant message.
        else:
            return("Passwords do no match")

class Menu:
    def __init__(self):
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
                user.reg_user(input("New Username: "), input("New Password: "), input("Confirm Password: "))

            elif menu == 'a':
                task.add_task(input("Name of person assigned to task: "), input("Title of Task: "), input("Description of Task: "))
                
            elif menu == 'va':
                task.view_all(task.task_list)
                    
            elif menu == 'vm':
                task.view_mine(task.task_list)                
    
            elif menu == "gr":
                task.generate_report(task.task_list)

            elif menu == "ds":
                task.display_stats("task_overview.txt", "user_overview.txt")
            
            elif menu == "e":
                exit()
            else:
                print("Choose a valid option")
                menu
# Instantiating the user object and creating user.txt file.    
user = User("user.txt")

# Instantiating the task object and creating user.txt file.    
task = Task("tasks.txt")

# Instantiating the menu object once .txt files have been created and read, ready to edit or display.
menu = Menu()