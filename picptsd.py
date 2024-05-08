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

background_image=tk.PhotoImage(file="hp pic 11.png")
background_label=tk.Label(root,image=background_image)
background_label.place(relwidth=1,relheight=1)

f1=tk.Frame(root, borderwidth=8,bg="#104E8B")
f1.pack(side='top',fill='x')

l=tk.Label(f1,text="POST TRAUMATIC STRESS DISORDER",fg="#F0FFF0",bg="#104E8B",font=("Comic Sans MS","30" ," bold"))
l.pack()

intro= '''  Based on the slim available evidence base, it is estimated that
                globally about 354 million adult survivors of war suffer from PTSD and/or MD,
                of which about 117 million are estimated to suffer from comorbid PTSD and MD
                                    '''
introduction =tk.Label(root,text=intro,bg='#F0FFF0',fg='#104E8B',font=('calibri',25),justify='center')
introduction.place(x=150,y=200)
