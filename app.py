import tkinter as tk
from tkinter import filedialog, Text
import os


root = tk.Tk()
apps = []

if os.path.isfile('save.txt'): #Remove extra space under the chosen apps
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]

def addApp():
    for widget in frame.winfo_children():
        widget.destroy() #Destroys widgets from the frame from the prevouse button use 

    #Will allow us to open the file directory, select an application, and add it to ours
    file_name = filedialog.askopenfilename(initialdir="/", title="Select File", filetypes=(("executables", "*.exe"), ("all files", "*.*"))) #Filetypes chosen limits us to only selecting executables
    apps.append(file_name) #Appends the path of the application we selected to the apps list
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack() #add the new app selected plus the prevouse apps chosen befor


canvas = tk.Canvas(root, height=700, width=700, bg="#263D42") 
canvas.pack()

frame= tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

open_file_button = tk.Button(root, text="Open File", padx=10, pady=5, fg="white", bg="#263D42", command=addApp) #Be descriptive with names \ Command is used to link the button to a function/method that will allow it to do stuff DO NOT ADD THE () WHEN CALLING THE FUNCTION OR IT WILL RUN THE FUNCTION AS SOON AS THE WINDOW LOADS!!!!
open_file_button.pack()

run_apps_button = tk.Button(root, text="Run Applications", padx=10, pady=5, fg="white", bg="#263D42")
run_apps_button.pack()

for app in apps:  #Puts the data on the save file from ours screen
    label = tk.Label(frame, text=app)
    label.pack()

root.mainloop()

#Create save file four chosen apps
with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',') 