import datetime as dt
import pandas as pd
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
        
        # Saves changes
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
        while True:
            try:
                date = dt.datetime.strptime(date, "%m/%d/Y")
            except ValueError:
                date = input("Invalid input, please try again: ")
            

    def user():
        
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

            # User input for the Task Manager
            if user == 1:
                task = input("Task: ")
                description = input("Description: ")
                date = input("Enter Date (MM/DD/YYYY): ")
                priority = input("Low-Medium-High:")
                TaskManager.add_tasks(task, description, date, priority)

            # Views the tasks
            elif user == 2:
                TaskManager.view_tasks()

            # Edit the tasks
            elif user == 3:
                TaskManager.view_tasks()
                editor = input("Which would you like to edit: ")

                task = input("Task: ")
                description = input("Description: ")
                date = input("Enter Date (MM/DD/YYYY): ")
                priority = input("Low-Medium-High:")
                TaskManager.edit_tasks(editor, task, description, date, priority)

            # Deletes the tasks
            elif user == 4:
                user = int(input("Which task would you like to delete: "))
                TaskManager.delete_tasks(user)

            # Searches the tasks by priority
            elif user == 5:
                priority_value = input("Filter from Low/Medium/High: ")
                TaskManager.search_tasks(priority_value)

            # Clears the tasks
            elif user == 6:
                TaskManager.clear_tasks()

            # Exits the Task Manager
            elif user == 7:
                print("Exiting...")
                break
                
            else:
                print("Invalid choice, please try again.")


if __name__ == "__main__":
    TaskManager.user()
























import unittest
import pandas as pd
import os
from TaskManager import create_file, add_task, view_tasks, edit_task, delete_task, search_tasks, clear_tasks, date_format

class TestTaskManager(unittest.TestCase):

    def setUp(self):
        # Create a test CSV file
        self.test_file = 'test_tasks.csv'
        global file_name
        file_name = self.test_file
        create_file()

    def tearDown(self):
        # Remove the test CSV file after each test
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add_task(self):
        add_task('Test Task', 'Test Description', date_format('01/01/2023'), 'High')
        df = pd.read_csv(self.test_file)
        self.assertEqual(len(df), 1)
        self.assertEqual(df.iloc[0]['Task'], 'Test Task')

    def test_view_tasks(self):
        add_task('Test Task 1', 'Description 1', date_format('01/01/2023'), 'High')
        add_task('Test Task 2', 'Description 2', date_format('02/01/2023'), 'Low')
        view_tasks()
        df = pd.read_csv(self.test_file)
        self.assertEqual(len(df), 2)

    def test_edit_task(self):
        add_task('Test Task', 'Test Description', date_format('01/01/2023'), 'High')
        edit_task(0, 'Edited Task', 'Edited Description', date_format('01/02/2023'), 'Medium')
        df = pd.read_csv(self.test_file)
        self.assertEqual(df.iloc[0]['Task'], 'Edited Task')

    def test_delete_task(self):
        add_task('Test Task', 'Test Description', date_format('01/01/2023'), 'High')
        delete_task(0)
        df = pd.read_csv(self.test_file)
        self.assertEqual(len(df), 0)

    def test_search_tasks(self):
        add_task('Test Task 1', 'Description 1', date_format('01/01/2023'), 'High')
        add_task('Test Task 2', 'Description 2', date_format('02/01/2023'), 'Low')
        search_tasks('High')
        df = pd.read_csv(self.test_file)
        filtered_df = df[df["Priority"].isin(['High'])]
        self.assertEqual(len(filtered_df), 1)

    def test_clear_tasks(self):
        add_task('Test Task', 'Test Description', date_format('01/01/2023'), 'High')
        clear_tasks()
        self.assertFalse(os.path.exists(self.test_file))

if __name__ == '__main__':
    unittest.main()