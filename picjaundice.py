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

background_image=tk.PhotoImage(file="hp pic 6.png")
background_label=tk.Label(root,image=background_image)
background_label.place(relwidth=1,relheight=1)

f1=tk.Frame(root, borderwidth=8,bg="#104E8B")
f1.pack(side='top',fill='x')

l=tk.Label(f1,text="JAUNDICE",fg="#F0FFF0",bg="#104E8B",font=("Comic Sans MS","29" ," bold"))
l.pack()

intro= ''' Jaundice is the most common condition requiring medical attention in newborn infants.
    About 50 percent of term and 80 percent of preterm infants develop
     jaundice in the first week of life.
     1 )Jaundice also is a common cause of readmission to the
      hospital after early discharge of newborn infants.
     2) Jaundice usually appears two to four days after birth and
    disappears one to two weeks later, usually without the need for treatment.
                    '''
introduction =tk.Label(root,text=intro,bg='#F0FFF0',fg='#104E8B',font=('calibri',25),justify='center')
introduction.place(x=150,y=200)
