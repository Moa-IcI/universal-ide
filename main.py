#!/usr/bin/env python3
import tkinter as tk
import os

command = None

root = tk.Tk()
root.title("Main Window")
root.geometry("600x400")

# ---------- buttons at the top ----------
topbar = tk.Frame(root)
topbar.pack(fill="x")

# ---------- Save logic ----------
def save_file(file_entry, win):
    filename = file_entry.get().strip()
    content = text_box.get("1.0", "end-1c")

    if not filename:
        print("No filename!")
        return

    print("Filename:", filename)
    print("Content:")
    print(content)


    contentfile = open(filename, 'w')
    contentfile.write(content)
    win.destroy()
def save_temp(file_entry, win):
    global command
    command = file_entry.get().strip()
    content = text_box.get("1.0", "end-1c")

    if not command:
        print("No input")
        return

    print("Command:", command)
    print("Content:")
    print(content)

    win.destroy()

def openthefile(filepath):
    with open(filepath, "r") as f:
        loadedfilecontent = f.read()

    text_box.delete("1.0", "end")
    text_box.insert("1.0", loadedfilecontent)
    if not filename:
        print("No filename!")
        return

# ---------- Windows ----------
def open_window_save():
    win = tk.Toplevel(root)
    win.title("Save script")

    tk.Label(win, text="Save script", font=("Arial", 14)).pack(padx=20, pady=20)

    file_entry = tk.Entry(win)
    file_entry.pack(padx=20, pady=10, fill="x")

    tk.Button(
        win,
        text="Save",
        command=lambda: save_file(file_entry, win)
    ).pack(pady=10)

def open_window_open():
    win = tk.Toplevel(root)
    win.title("Open File")
    file_entry = tk.Entry(win)
    file_entry.pack(padx=20, pady=10, fill="x")
    tk.Label(win, text="If you open a file EVERYTHING in the input box\nwill get deleted. So save what you want saved before opening anything").pack(padx=20)
    tk.Button(win, text="Open", command=lambda: openthefile(file_entry.get())).pack(pady=10)

def open_window_view():
    win = tk.Toplevel(root)
    win.title("View menu")
    tk.Label(win, text="This is the View menu!", font=("Arial", 14)).pack(padx=20, pady=20)

def open_window_prompt():
    win = tk.Toplevel(root)
    win.title("EXE Prompt")
    tk.Label(
        win,
        text="Command to execute to run script",
        font=("Arial", 14)
    ).pack(padx=20, pady=20)

    file_entry = tk.Entry(win)
    file_entry.pack(padx=20, pady=10, fill="x")
    tk.Label(win, text="If you want to launch your code but you need multiple lines,\nyou can create a .sh script or separate every command with a semi-column").pack(padx=20)
    tk.Button(win, text="Save", command=lambda: save_temp(file_entry, win)).pack(pady=10)

def open_window_run():
    content = text_box.get("1.0", "end-1c")
    if not command:
        print("No command defined. Use Shell Prompt first.")
        return
    print("Remember to save your work. Running does not save.")
    print("Running...")
    print(os.system(command))

# ---------- Top buttons ----------
tk.Button(topbar, text="Save", command=open_window_save).pack(side="left", padx=5, pady=5)
tk.Button(topbar, text="Open", command=open_window_open).pack(side="left", padx=5, pady=5)
tk.Button(topbar, text="View", command=open_window_view).pack(side="left", padx=5, pady=5)
tk.Button(topbar, text="Shell Prompt", command=open_window_prompt).pack(side="left", padx=5, pady=5)
tk.Button(topbar, text="Run", command=open_window_run).pack(side="right", padx=5, pady=5)

# ---------- Resizable Text Box ----------
text_box = tk.Text(root, wrap="none")

ys = tk.Scrollbar(root, orient="vertical", command=text_box.yview)
xs = tk.Scrollbar(root, orient="horizontal", command=text_box.xview)

text_box.configure(yscrollcommand=ys.set, xscrollcommand=xs.set)

ys.pack(side="right", fill="y")
xs.pack(side="bottom", fill="x")
text_box.pack(side="left", fill="both", expand=True)

root.mainloop()
