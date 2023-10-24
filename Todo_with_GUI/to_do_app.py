import tkinter as tk
from datetime import datetime

def add_task():
    task = entry_task.get()
    due_date = datetime.strptime(entry_due_date.get(), "%Y-%m-%d")
    priority = var_priority.get()
    
    tasks.append({"task": task, "due_date": due_date, "priority": priority})
    list_tasks()
    entry_task.delete(0, tk.END)
    entry_due_date.delete(0, tk.END)
    var_priority.set(priority_options[0])
    save_tasks()

def remove_task():
    selected = task_list.curselection()
    if selected:
        index = selected[0]
        del tasks[index]
        list_tasks()
        save_tasks()

def list_tasks():
    task_list.delete(0, tk.END)
    for i, task in enumerate(tasks, start=1):
        formatted_due_date = task['due_date'].strftime("%Y-%m-%d")
        task_list.insert(tk.END, f"{i}. Priority: {task['priority']} | {task['task']} (Due: {formatted_due_date})")

def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(f"{task['task']},{task['due_date']},{task['priority']}\n")

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                task_data = line.strip().split(",")
                task = {"task": task_data[0], "due_date": datetime.strptime(task_data[1], "%Y-%m-%d"), "priority": task_data[2]}
                tasks.append(task)
    except FileNotFoundError:
        return

tasks = []
priority_options = ["High", "Medium", "Low"]

load_tasks()  # Load tasks from the file when the app starts

root = tk.Tk()
root.title("To-Do List")

label_task = tk.Label(root, text="Task:")
entry_task = tk.Entry(root)

label_due_date = tk.Label(root, text="Due Date (YYYY-MM-DD):")
entry_due_date = tk.Entry(root)

label_priority = tk.Label(root, text="Priority:")
var_priority = tk.StringVar(root)
var_priority.set(priority_options[0])
priority_menu = tk.OptionMenu(root, var_priority, *priority_options)

add_button = tk.Button(root, text="Add Task", command=add_task)
remove_button = tk.Button(root, text="Remove Task", command=remove_task)
task_list = tk.Listbox(root)

label_task.pack()
entry_task.pack()
label_due_date.pack()
entry_due_date.pack()
label_priority.pack()
priority_menu.pack()
add_button.pack()
remove_button.pack()
task_list.pack()

root.mainloop()

