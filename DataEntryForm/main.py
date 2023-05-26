#Data Entry Form
#Author: Laszlo Koosz

import tkinter
from tkinter import ttk #themed widgets
from tkinter import messagebox

window = tkinter.Tk()
window.title("Data Entry Form")
window.geometry("800x600")

frame = tkinter.Frame(window)
frame.pack()

#saving user info
user_info_frame = tkinter.LabelFrame(frame, text="User Information")
user_info_frame.grid(row=0, column=0, padx=20, pady=20)

first_name_label = tkinter.Label(user_info_frame, text="First name")
first_name_label.grid(row=0, column=0)

last_name_label = tkinter.Label(user_info_frame, text="Last name")
last_name_label.grid(row=0, column=1)

first_name_entry = tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

title_label = tkinter.Label(user_info_frame, text="Title")
title_list = ["", "Mr.", "Ms.", "Dr."]
title_combobox = ttk.Combobox(user_info_frame, values=title_list)
title_label.grid(row=0, column=2)
title_combobox.grid(row=1, column=2)

age_label = tkinter.Label(user_info_frame, text="Age")
age_spinbox = tkinter.Spinbox(user_info_frame, from_=19, to=100)
age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)

nationality_label = tkinter.Label(user_info_frame, text="Nationality")
nationality_combobox = ttk.Combobox(user_info_frame, values=["English", "French", "Italian"])
nationality_label.grid(row=2, column=1)
nationality_combobox.grid(row=3, column=1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

#saving course info
courses_frame = tkinter.LabelFrame(frame, text="Course info")
courses_frame.grid(row=1, column=0, sticky="news", padx=20, pady=20)

registered_label = tkinter.Label(courses_frame, text="Registration status")

registered_check_var = tkinter.StringVar(value="Not registered")
registered_check = tkinter.Checkbutton(courses_frame, text="Currently registered",
                                       variable=registered_check_var, onvalue="Registered", offvalue="Not registered")
registered_label.grid(row=0, column=0)
registered_check.grid(row=1, column=0)

numsemesters_label = tkinter.Label(courses_frame, text="# Semesters")
numsemesters_spinbox = tkinter.Spinbox(courses_frame, from_=0, to="infinity")
numsemesters_label.grid(row=0, column=2)
numsemesters_spinbox.grid(row=1, column=2)

for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Accept terms
terms_frame = tkinter.LabelFrame(frame, text="Terms & Conditions")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=20)

terms_check_var = tkinter.StringVar(value="Not accepted")
terms_check = tkinter.Checkbutton(terms_frame, text="I accept the terms and conditions",
                                  variable=terms_check_var, onvalue="Accepted", offvalue="Not accepted")
terms_check.grid(row=0, column=0)

#Button
def button_clicked():
    #gather all the data from the form
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    title = title_combobox.get()
    age = age_spinbox.get()
    nationality = nationality_combobox.get()
    registration_status = registered_check_var.get()
    num_semesters = numsemesters_spinbox.get()
    terms_accepted = terms_check_var.get()

    if terms_accepted == "Not accepted":
        messagebox.showwarning(message="Please accept Terms & Conditions")
    elif len(first_name) < 1:
        messagebox.showwarning(message="Please enter a valid first name")
    elif len(last_name) < 1:
        messagebox.showwarning(message="Please enter a valid last name")
    elif title == "":
        messagebox.showwarning(message="Please select a title")
    elif nationality == "":
        messagebox.showwarning(message="Please select a nationality")
    else:

        #print data
        print("******************************")
        print(f"Title: {title}")
        print(f"Name: {first_name} {last_name}")
        print(f"Age: {age}")
        print(f"Nationality: {nationality}")
        print(f"Registration: {registration_status}")
        print(f"Number of semesters: {num_semesters}")
        print("******************************")

        #write data in to a file
        file = open("entries.txt", "a")
        file.write("******************************\n")
        file.write(f"Title: {title}\n")
        file.write(f"Name: {first_name} {last_name}\n")
        file.write(f"Age: {age}\n")
        file.write(f"Nationality: {nationality}\n")
        file.write(f"Registration: {registration_status}\n")
        file.write(f"Number of semesters: {num_semesters}\n")
        file.write("******************************\n")
        file.close()

        #display message
        messagebox.showinfo(message=f"Data entry is complete")



button = tkinter.Button(frame, text="Enter data", command=button_clicked)
button.grid(row=3, column=0)

window.mainloop()