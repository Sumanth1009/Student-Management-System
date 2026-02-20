import tkinter as tk

def delete_student():
    selected = student_listbox.curselection()
    if selected:
        student_listbox.delete(selected)
        message_label.config(text="Student deleted successfully", fg="green")
    else:
        message_label.config(text="Select a student to delete", fg="red")

def add_student():
    name = name_entry.get()
    age = age_entry.get()
    course = course_var.get()
    gender = gender_var.get()

    if name == "" or age == "" or course == "Select Course" or gender == "":
        message_label.config(text="Please fill all fields", fg="red")
        return

    if not age.isdigit():
        message_label.config(text="Age must be a number", fg="red")
        return

    student_data = f"Name: {name} | Age: {age} | Course: {course} | Gender: {gender}"
    student_listbox.insert(tk.END, student_data)

    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    course_var.set("Select Course")
    gender_var.set("")

root = tk.Tk()
root.title("Student Management System")
root.geometry("600x500")

title_label = tk.Label(root, text="Student Management System",
                       font=("Arial", 16, "bold"))
title_label.pack(pady=10)

form_frame = tk.Frame(root)
form_frame.pack(pady=10)

tk.Label(form_frame, text="Name").grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(form_frame)
name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(form_frame, text="Age").grid(row=1, column=0, padx=10, pady=5)
age_entry = tk.Entry(form_frame)
age_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(form_frame, text="Course").grid(row=2, column=0, padx=10, pady=5)
course_var = tk.StringVar()
course_var.set("Select Course")
course_menu = tk.OptionMenu(form_frame, course_var, "IT", "CSE", "ECE", "MECH", "CIVIL")
course_menu.grid(row=2, column=1, padx=10, pady=5)

tk.Label(form_frame, text="Gender").grid(row=3, column=0, padx=10, pady=5)
gender_var = tk.StringVar()
male_radio = tk.Radiobutton(form_frame, text="Male", variable=gender_var, value="Male")
female_radio = tk.Radiobutton(form_frame, text="Female", variable=gender_var, value="Female")
male_radio.grid(row=3, column=1, sticky="w")
female_radio.grid(row=3, column=1, padx=70, sticky="w")

add_button = tk.Button(root, text="Add Student", command=add_student)
add_button.pack(pady=10)

message_label = tk.Label(root, text="", font=("Arial", 10))
message_label.pack()

student_listbox = tk.Listbox(root, width=80, height=10)
student_listbox.pack(pady=10)

delete_button = tk.Button(root, text="Delete Selected", command=delete_student)
delete_button.pack(pady=10)
root.mainloop()
