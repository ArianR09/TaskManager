import datetime as dt
import pandas as pd
import tkinter as tk
import os

# File name for the csv file
file_name = "Task_Manager.csv"

# Class for the Task Manager
class TaskManager:
    
    def create_file():
        
        # Checks if the file exists, if not it creates a new file
        if not os.path.exists(file_name):
            df = pd.DataFrame(columns=["Task", "Description", "Date", "Priority"])
            df.to_csv(file_name, index=False)


    def add_tasks(task, description, date, priority):
        
        # Reads the csv file and adds the new task to the file
        df = pd.read_csv(file_name)

        new_task = pd.DataFrame({
            'Task': [task],
            'Description': [description],
            'Date': [date],
            'Priority': [priority]
        })

        df = pd.concat([df, new_task], ignore_index=True)
        df.to_csv(file_name, index=False)
        print("Task Added Successfully")
        

    def view_tasks():
        
        # Reads the csv file and sorts the tasks by date and priority
        df = pd.read_csv(file_name)
        
        df['Date'] = pd.to_datetime(df['Date'])
        df = df.sort_values(by=['Date', 'Priority'], ascending=[True, True])
        
        # Fixes readability
        df = df.reset_index(drop=True)
        print(df)
    
    def edit_tasks(num, task, description, date, priority):

        # Reads the csv file and edits the task in the file
        df = pd.read_csv(file_name)
        
        # Makes sure task in range
        if num in df.index:
            # Edits at specific index
            df.at[num, 'Task'] = task
            df.at[num, 'Description'] = description
            df.at[num, 'Date'] = date
            df.at[num, 'Priority'] = priority

            df.to_csv(file_name, index=False)
            print("Successfully edited.")
        else:
            print("Invalid index, please try again.")

    def delete_tasks(num):

        # Reads the csv file and deletes the task from the file
        df = pd.read_csv(file_name)
        
        if num in df.index:
            df = df.drop(df.index[num])

            df.to_csv(file_name, index=False)
            print("Task successfully removed.")
        else:
            print("Invalid task number.")

    def search_tasks(name):
        
        # Reads the csv file and filters between first index to highest
        df = pd.read_csv(file_name)
        filtered_df = df[df["Priority"].isin([name])]
        print(filtered_df)
            
        
    def clear_tasks():
        
        # Removes the file (clears)
        os.remove(file_name)
        print("File has been successfully cleared.")


    def date_format(date):

        # Sets up datetime format 
        return dt.datetime.strptime(date, "%m/%d/%Y")

    def main():
        
        # Creates the file if it does not exist
        TaskManager.create_file()

        while True:
            
            # Menu for the Task Manager
            print("MENU")
            print("1. Add Tasks")
            print("2. View Tasks")
            print("3. Edit Tasks")
            print("4. Delete Tasks")
            print("5. Search Tasks")
            print("6. Clear Tasks")
            print("7. Exit")

            user = int(input("Select one of the following: "))


            if user == 1:
                task = input("Task: ")
                description = input("Description: ")
                date = input("Enter Date (MM/DD/YYYY): ")
                priority = input("Low-Medium-High:")
                TaskManager.add_tasks(task, description, date, priority)

            elif user == 2:
                TaskManager.view_tasks()

            elif user == 3:
                TaskManager.view_tasks()
                editor = input("Which would you like to edit: ")

                task = input("Task: ")
                description = input("Description: ")
                date = input("Enter Date (MM/DD/YYYY): ")
                priority = input("Low-Medium-High:")
                TaskManager.edit_tasks(editor, task, description, date, priority)

            elif user == 4:
                user = int(input("Which task would you like to delete: "))
                TaskManager.delete_tasks(user)

            elif user == 5:
                priority_value = input("Filter from Low/Medium/High: ")
                TaskManager.search_tasks(priority_value)

            elif user == 6:
                TaskManager.clear_tasks()

            elif user == 7:
                print("Exiting...")
                break
                
            else:
                print("Invalid choice, please try again.")
            
class UI:

    label = tk.Label(
        foreground="white",
        background="black"
    )

if __name__ == "__main__":
    TaskManager.main()


    
# Class for the User Interface
