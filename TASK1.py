from tkinter import *
from tkinter import messagebox
import sqlite3 as sql

# Database Operations
class TaskDatabase:
    def __init__(self, db_name='listOfTasks.db'):
        self.conn = sql.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS tasks (title TEXT, completed INTEGER)')

    def add_task(self, task):
        self.cursor.execute('INSERT INTO tasks (title, completed) VALUES (?, ?)', (task, 0))
        self.conn.commit()

    def delete_task(self, task):
        self.cursor.execute('DELETE FROM tasks WHERE title = ?', (task,))
        self.conn.commit()

    def delete_all_tasks(self):
        self.cursor.execute('DELETE FROM tasks')
        self.conn.commit()

    def get_tasks(self):
        self.cursor.execute('SELECT title, completed FROM tasks')
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()

# GUI for Task Management
class TaskManager:
    def __init__(self, root):
        self.db = TaskDatabase()
        self.tasks = []

        # Get screen width and height
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        window_width = int(screen_width * 0.5)  # 50% of screen width
        window_height = int(screen_height * 0.5)  # 50% of screen height
        x_pos = (screen_width - window_width) // 2
        y_pos = (screen_height - window_height) // 3

        # Window setup
        root.title("To-Do List")
        root.geometry(f"{window_width}x{window_height}+{x_pos}+{y_pos}")  
        root.resizable(True, True)
        root.configure(bg="#B5E5CF")

        # Frame
        self.functions_frame = Frame(root, bg="#8EE5EE")
        self.functions_frame.pack(expand=True, fill="both")

        # Widgets
        self.create_widgets()
        self.retrieve_database()
        self.update_listbox()

    def create_widgets(self):
        Label(
            self.functions_frame,
            text="TO-DO LIST \nEnter the Task Title:",
            font=("Arial", 14, "bold"),
            bg="#8EE5EE", fg="#FF6103"
        ).place(relx=0.05, rely=0.05)

        self.task_field = Entry(
            self.functions_frame,
            font=("Arial", 14),
            bg="white"
        )
        self.task_field.place(relx=0.3, rely=0.07, relwidth=0.6, height=30)

        Button(
            self.functions_frame, text="Add Task",
            bg='#D4AC0D', font=("Arial", 12, "bold"),
            command=self.add_task
        ).place(relx=0.05, rely=0.18, relwidth=0.25, height=35)

        Button(
            self.functions_frame, text="Remove Task",
            bg='#D4AC0D', font=("Arial", 12, "bold"),
            command=self.delete_task
        ).place(relx=0.35, rely=0.18, relwidth=0.25, height=35)

        Button(
            self.functions_frame, text="Delete All",
            bg='#D4AC0D', font=("Arial", 12, "bold"),
            command=self.delete_all_tasks
        ).place(relx=0.65, rely=0.18, relwidth=0.25, height=35)

        self.task_listbox = Listbox(
            self.functions_frame, font=("Arial", 12),
            bg="WHITE", fg="BLACK",
            selectbackground="#FF8C00", selectforeground="BLACK"
        )
        self.task_listbox.place(relx=0.05, rely=0.3, relwidth=0.9, relheight=0.5)

        Button(
            self.functions_frame, text="Exit / Close",
            bg='#D4AC0D', font=("Arial", 12, "bold"),
            command=self.close
        ).place(relx=0.05, rely=0.85, relwidth=0.9, height=35)

    def add_task(self):
        task = self.task_field.get().strip()
        if not task:
            messagebox.showinfo('Error', 'Field is Empty.')
            return

        if task in self.tasks:
            messagebox.showinfo('Error', 'Task already exists.')
            return

        self.tasks.append(task)
        self.db.add_task(task)
        self.update_listbox()
        self.task_field.delete(0, 'end')

    def delete_task(self):
        try:
            selected_task = self.task_listbox.get(self.task_listbox.curselection())
            if selected_task in self.tasks:
                self.tasks.remove(selected_task)
                self.db.delete_task(selected_task)
                self.update_listbox()
        except:
            messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.')

    def delete_all_tasks(self):
        if messagebox.askyesno('Delete All', 'Are you sure?'):
            self.tasks.clear()
            self.db.delete_all_tasks()
            self.update_listbox()

    def update_listbox(self):
        self.task_listbox.delete(0, 'end')
        for task in self.tasks:
            self.task_listbox.insert('end', task)

    def retrieve_database(self):
        self.tasks.clear()
        for task, completed in self.db.get_tasks():
            self.tasks.append(task)

    def close(self):
        self.db.close()
        guiWindow.destroy()

if __name__ == "__main__":
    guiWindow = Tk()
    app = TaskManager(guiWindow)
    guiWindow.mainloop()
