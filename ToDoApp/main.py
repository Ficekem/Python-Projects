#ToDo App
#Author: Laszlo Koosz
#https://github.com/Ficekem
#https://www.linkedin.com/in/laszlo-koosz-235654267/

#we are using the CustomTkinter library by Tom Schimansky
#https://github.com/TomSchimansky/CustomTkinter
import customtkinter as ctk
import getpass #it is required to get current user name
from packaging import * #when packaged using pyinstaller, we are required to manually import packages

#****************************
#variables
#****************************

#get user name
USER_NAME = getpass.getuser()
#variable to check if this is the first time the application run
AT_THE_BEGINNING = True
#variable to store name and path of file where to store our data, for now we use the Desktop
STORAGE = f"/Users/{USER_NAME}/Desktop/tasks.txt" #macOS (add Windows path when packaged for Windows)

#****************************
#functions
#****************************

def save_todo():

    #erase file to make sure only the most up to date list is stored
    file = open(STORAGE, "w").close()

    #find the label widgets within the scrollable frame
    for frame in scrollable_frame.winfo_children():
        for widget in frame.winfo_children():
            if isinstance(widget, ctk.CTkLabel):
                #write text of each label in to file
                file = open(STORAGE, "a")
                file.write(f"{widget.cget('text')}\n")

    file.close()
                   
def delete_todo(item, content):
    #make item invisible
    #item.pack_forget()
    #permanently delete item
    item.destroy()
    #save the list
    save_todo()

def add_todo(_text=""):

    def add(t):
        #create an empty frame within the scrollable frame to store the content and a checkbox
        frame = ctk.CTkFrame(scrollable_frame)
        #create a label in the empty frame
        label = ctk.CTkLabel(frame, text=t, font=ctk.CTkFont(size=18), width=670)
        #create a checkbox in the empty frame
        delete_check = ctk.CTkCheckBox(frame, text="", command= lambda: delete_todo(frame, label))

        #package all up
        frame.pack()
        label.grid(row=0,column=1)
        delete_check.grid(row=0, column=0)

        #delete the content of the entry from first to last character
        entry.delete(0, ctk.END)

        #save list in to file
        save_todo()

    #get the content of the entry
    todo = entry.get()

    # if the content is not empty
    if todo != "":
        add(todo)
    else: #if the content was empty, check if we passed any text
        if _text != "":
            add(_text)

def check_keypress(event):
    #if return key is pressed, add todo to list 
    if event.keysym == "Return":
        add_todo()



#****************************
#main program
#****************************

#create window
window = ctk.CTk()
window.geometry("750x450")
window.title("ToDo App")

#title label
title_label = ctk.CTkLabel(window, text="Daily Tasks", font=ctk.CTkFont(size=20, weight="bold"))
title_label.grid(row=0, column=0, padx=10, pady=10)

#scrollable frame
scrollable_frame = ctk.CTkScrollableFrame(window, width=700, height=370)
scrollable_frame.grid(row=1, column=0, padx=10, pady=(0,20))

#an empty container to store the entry and the button
entry_container = ctk.CTkFrame(scrollable_frame, width=700)
entry_container.pack()

#add entry to entry container
entry = ctk.CTkEntry(entry_container, placeholder_text="Add item", width=670)
entry.grid(row=0, column=0, padx=(0, 5))

#add button to entry container
add_button = ctk.CTkButton(entry_container, text="+ ",font=ctk.CTkFont(size=18, weight="bold") , width=30, command=add_todo)
add_button.grid(row=0, column=1)

#bind key press event to the method check_keypress
window.bind("<KeyPress>", check_keypress)

#if this is the first time the application run, attempt to load the list from file
if AT_THE_BEGINNING:
    try:
        #attempt to open the file that store our list and read each line
        file = open(STORAGE, "r")
        lines = file.read().splitlines() #splitlines to remove \n
        file.close()

        #add each line to todo list
        for line in lines:
            add_todo(line)

    except FileNotFoundError:
        print(f"Failed to open {STORAGE}")
    
    #set variable to false to make sure we no longer attempt to load the list from file
    AT_THE_BEGINNING = False

#update the window
window.mainloop()