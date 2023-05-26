#recipe picker
#Author: Laszlo Koosz

import tkinter as tk
from PIL import ImageTk #PIL is an image library but out of date, installed Pillow instead
import sqlite3
from numpy import random

#initialise app
root = tk.Tk()
root.title("RecipePicker")
bg_color = "#3d6466"

def clear_widgets(frame):
    for widget in frame.winfo_children():
        widget.destroy()


def fetch_db():

    #connect to database
    connection = sqlite3.connect("data/recipes.db")
    cursor = connection.cursor()

    #get all tables from database
    cursor.execute("SELECT * FROM sqlite_schema WHERE type='table';")
    all_tables = cursor.fetchall()

    #pick a random table
    idx = random.randint(0, len(all_tables) - 1)

    #get ingredients from the selected table
    table_name = all_tables[idx][1]
    cursor.execute("SELECT * FROM " + table_name + ";")
    table_records = cursor.fetchall() #ingredients

    connection.close()

    return table_name, table_records

def pre_process(table_name, table_records):

    #process title
    title = table_name[:-6] #remove numbers from the end of the title
    #list comprehension, one liner for loop
    #add space between each word in the title
    #if char is lower do nothing, else add a " " for each char in title
    new_chars = [char if char.islower() else " " + char for char in title]
    title = "".join(new_chars) #update title to include new characters

    #process ingredients
    #data looks like this in table records
    #id, name, quantity, unit

    ingredients = []

    for i in table_records:
        name = i[1]
        quantity = i[2]
        unit = i[3]
        ingredients.append(quantity + " " + unit + " " + name)

    return title, ingredients
  

def load_frame1():
    clear_widgets(frame2)
    frame1.tkraise() #stack frame 1 on top of frame 2
    #this is to avoid other packs effect the frame. frame stay as is
    frame1.pack_propagate(False)

    #frame1 widgets
    logo_img = ImageTk.PhotoImage(file="assets/RRecipe_logo.png") #load image
    logo_widget = tk.Label(frame1, image=logo_img, bg=bg_color) #create widget with image
    logo_widget.image = logo_img #but then we need to assign the image compontent of the widget to the image once again
    logo_widget.pack()

    tk.Label(frame1,
            text="ready for your random recipe?",
            bg=bg_color,
            fg="white",
            font=("TkMenuFont", 14)
            ).pack()

    #button widget
    tk.Button(frame1,
            text="SHUFFLE",
            font=("TkHeadingFont", 20),
            bg="blue",
            fg="blue",
            cursor="hand2",
            activebackground="blue",
            activeforeground="blue",
            command=load_frame2
            ).pack(pady=20)


def load_frame2():
    clear_widgets(frame1)
    frame2.tkraise() #stack frame 2 on top of frame 1

    #load recipe from database
    table_name, table_records = fetch_db()
    title, ingredients = pre_process(table_name, table_records)

    #widgest
    logo_img = ImageTk.PhotoImage(file="assets/RRecipe_logo_bottom.png") #load image
    logo_widget = tk.Label(frame2, image=logo_img, bg=bg_color) #create widget with image
    logo_widget.image = logo_img #but then we need to assign the image compontent of the widget to the image once again
    logo_widget.pack(pady=20)

    tk.Label(frame2,
        text=title,
        bg=bg_color,
        fg="white",
        font=("TkHeadingFont", 20)
        ).pack(pady=25)
    
    for i in ingredients:
        tk.Label(frame2,
        text=i,
        bg="#28393a",
        fg="white",
        font=("TkMenuFont", 12)
        ).pack(fill="both") #fill to make the bg scale edge to edge
    
    #button widget
    tk.Button(frame2,
            text="BACK",
            font=("TkHeadingFont", 18),
            bg="blue",
            fg="blue",
            cursor="hand2",
            activebackground="blue",
            activeforeground="blue",
            command=load_frame1
            ).pack(pady=20)


#center window
#one way simple just one line and also auto adjust size to content
root.eval("tk::PlaceWindow . center")
#second way more complicated
#x = int(root.winfo_screenwidth() / 2) # in the middle
#y = int(root.winfo_screenheight() * 0.1) #10% from the top
#root.geometry("500x600+" + str(x) + "+" + str(y))

#create frames, it is like a page within the app
frame1 = tk.Frame(root, width=500, height=600, bg=bg_color)
frame2 = tk.Frame(root, bg=bg_color) #frame2 is the same size as frame1

#setup the grid for each frame to have only 1 column and 1 row meaning its using the entire window
for frame in (frame1, frame2):
    frame.grid(row=0, column=0, sticky="nesw") #nesw means when window size change, stick content to all 4 corners

#load frame 1
load_frame1()

#run app
root.mainloop()