import tkinter as tk
from tkinter import messagebox
from tkinter import Label
import random

root=tk.Tk()

root.geometry("750x500")

label1=Label(text="Rock,Paper,Scissors game!")
label1.pack()

root.title("Lets play!")

choices=["Rock","Paper","Scissors"]

def result(user,comp):
    
    if user==comp:
        return "Its a tie"


    elif user=="Rock" and comp=="Paper":
        return "Computer won"
        

    elif user=="Rock" and comp=="Scissors":
        return "You won"
        

    elif user=="Paper" and comp=="Rock":
        return "You won"
        

    elif user=="Paper" and comp=="Scissors":
        return "Computer won"
        

    elif user=="Scissors" and comp=="Rock":
        return "Computer won"
        

    elif user=="Scissors" and comp=="Paper":
        return "You won"
        

    else:
        return "Invalid input"

def play(user):
    comp=random.choice(choices)
    winner=result(user,comp)
    messagebox.showinfo("Result", f"You chose {user}\n Computer chose {comp}\n {winner}")



rock_button=tk.Button(root,text="Rock", command=lambda: play("Rock"), height=4,width=10)
rock_button.pack(pady=20)

paper_button=tk.Button(root,text="Paper", command=lambda: play("Paper"), height=4,width=10)
paper_button.pack(pady=20)

scissors_button=tk.Button(root,text="Scissors", command=lambda: play("Scissors"), height=4,width=10)
scissors_button.pack(pady=20)

root.mainloop()
        
    