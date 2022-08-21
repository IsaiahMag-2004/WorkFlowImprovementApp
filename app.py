import tkinter as tk #import and nickname the GUI framework
from tkinter import filedialog, Text
import os #Help interface with system


root = tk.Tk() #Create the frame of our app for us to add stuff to
apps = []

if os.path.isfile('save.txt'): #Removes the extra space that is under the chosen apps
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()] #Strips all the empty spaces

def addApp():
    for widget in frame.winfo_children():
        widget.destroy() #Destroys widgets from the frame from the prevouse button use 

    #Will allow us to open the file directory, select an application, and add it to ours
    file_name = filedialog.askopenfilename(initialdir="/", title="Select File", filetypes=(("executables", "*.exe"), ("all files", "*.*"))) #Filetypes chosen limits us to only selecting executables
    apps.append(file_name) #Appends the path of the application we selected to the apps list
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack() #Allone this loop will just add the new app selected plus the prevouse apps chosen befor


canvas = tk.Canvas(root, height=700, width=700, bg="#263D42") #Allows you to set the size of the window
canvas.pack() #Puts canvas on the screen

frame= tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1) #The rels put an equal amount of space between the edge and the frame centering it in this case

open_file_button = tk.Button(root, text="Open File", padx=10, 
                            pady=5, fg="white", bg="#263D42", command=addApp) #Be descriptive with names \ Command is used to link the button to a function/method that will allow it to do stuff DO NOT ADD THE () WHEN CALLING THE FUNCTION OR IT WILL RUN THE FUNCTION AS SOON AS THE WINDOW LOADS!!!!
open_file_button.pack()

run_apps_button = tk.Button(root, text="Run Applications", padx=10, 
                            pady=5, fg="white", bg="#263D42") #Be descriptive with names
run_apps_button.pack()

for app in apps:  #Puts the data from the save file from ours screen
    label = tk.Label(frame, text=app)
    label.pack()

root.mainloop() #Run all in the body of the application

#Create save file four chosen apps
with open('save.txt', 'w') as f: #Whenever we close the app were gonna save a text file written as f and with f we can write all the apps we saved in the app
    for app in apps:
        f.write(app + ',') 