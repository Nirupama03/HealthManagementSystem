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

l=tk.Label(f1,text="MIGRANE",fg="#F0FFF0",bg="#104E8B",font=("Comic Sans MS","30" ," bold"))
l.pack()

intro= '''  Everyone either knows someone who suffers from
            migraine, or struggles with migraine themselves.
            Migraine is the 3rd most prevalent illness in the world.
            Nearly 1 in 4 U.S. households includes someone with migraine.
            Amazingly, 12% of the population – including children – suffers from migraine.
            18% of American women, 6% of men, and 10% of children
            experience migraines.
            Migraine is most common between the ages of 18 and 44.
            Migraine tends to run in families. About 90% of migraine
            sufferers have a family history of migraine.
            Healthcare and lost productivity costs associated with
            migraine are estimated to be as high as $36 billion annually in the U.S.
             Migraine often goes undiagnosed in children.
                    '''
introduction =tk.Label(root,text=intro,bg='#F0FFF0',fg='#104E8B',font=('calibri',25),justify='center')
introduction.place(x=150,y=100)
