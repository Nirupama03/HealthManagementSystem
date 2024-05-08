import tkinter as tk
from tkinter import messagebox
import random as r
HEIGHT=1920
WIDTH=1080
root=tk.Tk()
canvas=tk.Canvas(root,height=HEIGHT,width=WIDTH)
canvas.place()
title=root.title("SOINS DE SANTE")


background_image=tk.PhotoImage(file="feedbackpic.png")
background_label=tk.Label(root,image=background_image)
background_label.place(relwidth=1,relheight=1)
f1=tk.Frame(root, borderwidth=8,bg="#104E8B")
f1.pack(side='top',fill='x')

l=tk.Label(f1,text="FEEDBACK",fg="#FFFAF0",bg="#104E8B",font=("Comic Sans MS","29" ," bold"))
l.pack()

frame=tk.Frame(root,padx=10,pady=10,bg='#104E8B')
frame.pack(padx=200,pady=200)

def submit():
        thankyou=messagebox.showinfo("THANKYOU!!!",
                                           '''THANKYOU FOR VISITING US ... YOUR FEEDBACK MATTERS A LOT TO US AND FEEL FREE TO CALL US ANYTIME ON 56789990 FOR QUERIES OR COMPLAINTS, KEEP VISITING US ''')                        
good= tk.Entry(frame,width=75,bd=6,bg='#FFFAF0',font=70)
bad=tk.Entry(frame,width=75,bd=6,bg='#FFFAF0',font=70)
good.insert(0," What were the highlights you were impressed by ? :")
bad.insert(0,"Any issues/queries/complaint you would want to report ?")
good.pack(padx=2,pady=2)
bad.pack(padx=2,pady=2)
         
mybutton=tk.Button(frame,text="SUBMIT",command=submit  ,width=10,font=40,bg="#8DB6CD",pady=20)
mybutton.pack()

  
         











         
