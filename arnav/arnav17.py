from tkinter import *

windows =  Tk()
windows.title('My Profile Card')
windows.geometry('400x380')

title = Label(windows, text='My profile card', fg='white', bg='purple', width=40)
title.grid(row = 0, column = 0, columnspan=2, padx=10, pady=10)


name_label = Label(windows, text='Name:', fg='black', bg='white')
name_label.grid(row=1, column=0, padx=10, pady=5)

name_entry = Entry(windows,fg='blue', bg='lightyellow', width=25)
name_entry.grid(row=1, column=1, padx=10, pady=5)

hobby_label = Label(windows, text='Hobby:', fg='black', bg='white')
hobby_label.grid(row=2, column=0, padx=10, pady=5)

hobby_entry = Entry(windows, fg='blue', bg='lightyellow', width=25)
hobby_entry.grid(row=1, column=0, padx=10, pady=5)

about_frame = Frame(windows, relief=RAISED, borderwidth=3)
about_frame.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

about_label = Label(about_frame, text='About Me:')
about_label.pack()

about_text = Text(about_frame, fg='green', bg='lightyellow', width=40, height=4)
about_text.pack()


submit = Button(windows, text='Show my card', bg='purple', fg='white', width=20)
submit.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

windows.mainloop()