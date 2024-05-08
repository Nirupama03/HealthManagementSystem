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

l=tk.Label(f1,text="ARTHRITIS",fg="#F0FFF0",bg="#104E8B",font=("Comic Sans MS","30" ," bold"))
l.pack()

intro= '''  From 2013 to 2015 in the United States
                Of people aged 18 to 44 years, 7.1% ever reported doctor-diagnosed arthritis.
                1 Of people aged 45 to 64 years, 29.3% ever reported doctor-diagnosed arthritis.
                1 Of people aged 65 years or older, 49.6% ever reported doctor-diagnosed arthritis.
                1 The risk of arthritis increases with age and arthritis is more common
                among women than men.
                1 Adults aged 18 years or older
                who are overweight or obese report doctor-diagnosed arthritis more often
                than adults with a lower body mass index (BMI).
                More than 16% of under/normal weight adults report doctor-diagnosed arthritis.1
                Almost 23% of overweight and 31% of obese US adults report doctor-diagnosed arthritis.1 
                    '''
introduction =tk.Label(root,text=intro,bg='#F0FFF0',fg='#104E8B',font=('calibri',20),justify='center')
introduction.place(x=150,y=100)
