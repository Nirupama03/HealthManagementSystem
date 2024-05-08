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

background_image=tk.PhotoImage(file="hp pic 5.png")
background_label=tk.Label(root,image=background_image)
background_label.place(relwidth=1,relheight=1)

f1=tk.Frame(root, borderwidth=8,bg="#104E8B")
f1.pack(side='top',fill='x')

l=tk.Label(f1,text="CHICKEN POX",fg="#F0FFF0",bg="#104E8B",font=("Comic Sans MS","30" ," bold"))
l.pack()

intro= '''  Chickenpox used to be very common in the United States.
                In the early 1990s, an average of 4 million people got varicella,
                10,500 to 13,000 were hospitalized (range, 8,000 to 18,000),
                and 100 to 150 died each year.
                In the 1990s, the highest rate of varicella was
                reported in preschool-aged children.
                Chickenpox vaccine became available in the United States in 1995.
                In 2014, 91% of children 19 to 35 months old in the United States had received
                one dose of varicella vaccine, varying from 83% to 95% by state.
                Among adolescents 13 to 17 years of age without a prior history of disease,
                95% had received 1 dose of varicella vaccine, and 81% had received
                2 doses of the vaccine.Eighty-five percent of adolescents
                had either a history of varicella disease or
                received 2 doses of varicella vaccine.

                Each year, more than 3.5 million cases of varicella,
                9,000 hospitalizations, and 100 deaths are
                prevented by varicella vaccination in the United States.
                    '''
introduction =tk.Label(root,text=intro,bg='#F0FFF0',fg='#104E8B',font=('calibri',"19"),justify='center')
introduction.place(x=150,y=100)
