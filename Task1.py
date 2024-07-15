import tkinter as tk
from tkinter import Label
from tkinter import messagebox
import random

root=tk.Tk()

root.geometry("900x650")

root.title("Daily to do list")

label1=Label(text="Enter your work to do today",font=("Arial",14))
label1.grid(row=1,column=1,columnspan=1,padx=20,pady=10)


entry=tk.Entry(root,width=40)
entry.grid(row=1,column=2,columnspan=2,pady=20,padx=20)

def click():
    user_text=entry.get()
    if user_text:
        listbox.insert(tk.END,user_text)
        messagebox.showinfo("Recently added item",f"Added : {user_text}")
        entry.delete(0,tk.END)

def delete():
    select_item=listbox.curselection()
    if select_item:
        for index in select_item[::-1]:
            listbox.delete(index)

def select_item(event):
    try:
        selected_index = listbox.curselection()[0]
        selected_text = listbox.get(selected_index)
        entry.delete(0, tk.END)
        entry.insert(0, selected_text)
    except IndexError:
        pass

button_add=tk.Button(root,text="Add",command=click,height=3,width=12)
button_add.grid(row=4,column=2,padx=(20,5),pady=10)

button_delete=tk.Button(root,text="Delete",command=delete,height=3,width=12)
button_delete.grid(row=4,column=3,padx=(5,20),pady=10)


listbox=tk.Listbox(root,height=25,width=40)
listbox.grid(row=5,column=2,columnspan=4,pady=40,padx=20)

listbox.bind('<<ListboxSelect>>', select_item)


root.mainloop()