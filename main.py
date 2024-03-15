from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
 
root = Tk()
root.geometry("500x300")
root.title("MySQL CRUD Operations")
id = Label(root, text="Enter ID:", font=("verdana 15"))
id.place(x=50, y=30)
id_entry = Entry(root, font=("verdana 15"))
id_entry.place(x=150, y=30)
  
name = Label(root, text="Name:", font=("verdana 15"))
name.place(x=50, y=80)
name_entry = Entry(root, font=("verdana 15"))
name_entry.place(x=150, y=80)
  
phone = Label(root, text="Phone:", font=("verdana 15"))
phone.place(x=50, y=130)
phone_entry= Entry(root, font=("verdana 15"))
phone_entry.place(x=150, y=130)
  
btnInsert = Button(root, text="Insert", command=Insert, font=("verdana 15")).place(x=100, y=190)
btnDelete = Button(root, text="Delete", command=Del, font=("verdana 15")).place(x=200, y=190)
btnUpdate = Button(root, text="Update", command=Update, font=("verdana 15")).place(x=320, y=190)
btnSelect= Button(root, text="Select", command=Select, font=("verdana 15")).place(x=200, y=240)
  
root.mainloop()