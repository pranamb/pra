import tkinter as tk
from tkinter import messagebox
import json
import os

# File to save tasks
TASKS_FILE = 'tasks.json'

# Load tasks from file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.tasks = load_tasks()

        # Create GUI components
        self.task_entry = tk.Entry(root, width=50)
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.task_listbox = tk.Listbox(root, width=50, height=10)
        self.task_listbox.pack(pady=10)

        self.mark_complete_button = tk.Button(root, text="Mark Complete", command=self.mark_complete)
        self.mark_complete_button.pack(side=tk.LEFT, padx=5)

        self.mark_incomplete_button = tk.Button(root, text="Mark Incomplete", command=self.mark_incomplete)
        self.mark_incomplete_button.pack(side=tk.LEFT, padx=5)

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(side=tk.LEFT, padx=5)

        self.update_listbox()

    def add_task(self):
        description = self.task_entry.get()
        if description:
            self.tasks.append({'description': description, 'completed': False})
            save_tasks(self.tasks)
            self.update_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Task description cannot be empty.")

    def mark_complete(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.tasks[index]['completed'] = True
            save_tasks(self.tasks)
            self.update_listbox()

    def mark_incomplete(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.tasks[index]['completed'] = False
            save_tasks(self.tasks)
            self.update_listbox()

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.tasks.pop(index)
            save_tasks(self.tasks)
            self.update_listbox()

    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "✔️" if task['completed'] else "❌"
            self.task_listbox.insert(tk.END, f"{task['description']} [{status}]")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()