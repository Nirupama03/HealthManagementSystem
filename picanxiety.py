import tkinter as tk
import mysql.connector as m
from tkinter import messagebox
from tkinter import ttk
import random as r 
import time as t


root=tk.Tk()
root.geometry("700x500")
title=root.title("SOINS DE SANTE")
photo=tk.PhotoImage(file='doc icon.png')
icon=root.iconphoto(False,photo)

background_image=tk.PhotoImage(file="final pic 2.png")
background_label=tk.Label(root,image=background_image)
background_label.place(relwidth=1,relheight=1)

f1=tk.Frame(root, borderwidth=8,bg="#104E8B")
f1.pack(side='top',fill='x')

l=tk.Label(f1,text="ANXIETY",fg="#F0FFF0",bg="#104E8B",font=("Comic Sans MS","30" ," bold"))
l.pack()

intro= '''  7 percent by country. Globally an estimated 284 million people
                experienced an anxiety disorder in 2017,
                making it the most prevalent mental health
                or neurodevelopmental disorder.
                Around 63 percent (179 million) were female,
                relative to 105 million males.
                                    '''
introduction =tk.Label(root,text=intro,bg='#F0FFF0',fg='#104E8B',font=('calibri',30),justify='center')
introduction.place(x=150,y=100)
