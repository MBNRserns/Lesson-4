from tkinter import *
root = Tk()
root.config(background="White")
root.title("Library Management System")
root.geometry("500x500")
root.config(background="gray")

Title=Label(root,text = "Book Title").place(x=40, y=20)
title_entry_area= Entry(root,width=30).place(x=110,y=20)

Name=Label(root,text = "Your Name").place(x=40, y=70)
Name_entry_area= Entry(root,width=30).place(x=110,y=70)

Surname=Label(root,text = "Your \r Surname").place(x=40, y=120)
Surname_entry_area= Entry(root,width=30).place(x=110,y=120)

borrowed=Label(root,text = "Date \rBorrowed").place(x=40, y=170)
borrowed_entry_area= Entry(root,width=30).place(x=110,y=170)

listbox=Label(root,text = "Date Due").place(x=40, y=170)
listbox =Listbox(root, height=10,width=15,bg="gray",activestyle='dotbox',font="Helvetica",fg="yellow")
listbox.insert(1, "5/9/2024")
listbox.insert(2, "10/9/2024")
listbox.insert(3, "15/9/2024")
listbox.insert(4, "20/9/2024")
listbox.insert(5, "25/9/2024")

listbox.pack()

root.mainloop()