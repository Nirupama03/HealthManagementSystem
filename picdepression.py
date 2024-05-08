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

background_image=tk.PhotoImage(file="hp pic 7.png")
background_label=tk.Label(root,image=background_image)
background_label.place(relwidth=1,relheight=1)

f1=tk.Frame(root, borderwidth=8,bg="#104E8B")
f1.pack(side='top',fill='x')

l=tk.Label(f1,text="DEPRESSION",fg="#F0FFF0",bg="#104E8B",font=("Comic Sans MS","30" ," bold"))
l.pack()

intro= '''  Depression is a common illness worldwide, with more than 264 million people affected(1).
                Depression is different from usual mood fluctuations and short-lived
                emotional responses to challenges in everyday life.
                Especially when long-lasting and with moderate or severe intensity,
                depression may become a serious health condition.
                It can cause the affected person to suffer greatly and function poorly at work,
                at school and in the family.
                At its worst, depression can lead to suicide. Close to 800 000 people die due to suicide every year.
                Suicide is the second leading cause of death in 15-29-year-olds
                                    '''
introduction =tk.Label(root,text=intro,bg='#F0FFF0',fg='#104E8B',font=('calibri',20),justify='center')
introduction.place(x=150,y=100)
