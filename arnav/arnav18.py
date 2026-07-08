import tkinter as tk
from tkinter import messagebox


def show_bio():
    bio = f"""
    PERSONAL BIO

    Name: {name_entry.get()}
    Age: {age_entry.get()}
    Gender: {gender_entry.get()}
    School: {school_entry.get()}
    Class: {class_entry.get()}
    Favourite Subject: {subject_entry.get()}
    Hobbies: {hobby_entry.get()}
    Future Career: {career_entry.get()}
    """
    messagebox.showinfo("Personal Bio", bio)

root = tk.Tk()
root.title("Personal Bio Form")
root.geometry("450x500")


title = tk.Label(root, text="Personal Bio Form", font=("Arial", 18, "bold"))
title.pack(pady=10)


tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root, width=35)
name_entry.pack()


tk.Label(root, text="Age").pack()
age_entry = tk.Entry(root, width=35)
age_entry.pack()

tk.Label(root, text="Gender").pack()
gender_entry = tk.Entry(root, width=35)
gender_entry.pack()


tk.Label(root, text="School").pack()
school_entry = tk.Entry(root, width=35)
school_entry.pack()


tk.Label(root, text="Class").pack()
class_entry = tk.Entry(root, width=35)
class_entry.pack()


tk.Label(root, text="Favourite Subject").pack()
subject_entry = tk.Entry(root, width=35)
subject_entry.pack()


tk.Label(root, text="Hobbies").pack()
hobby_entry = tk.Entry(root, width=35)
hobby_entry.pack()


tk.Label(root, text="Future Career").pack()
career_entry = tk.Entry(root, width=35)
career_entry.pack()


submit_btn = tk.Button(root, text="Show Bio", command=show_bio, bg="lightblue")
submit_btn.pack(pady=20)

root.mainloop()