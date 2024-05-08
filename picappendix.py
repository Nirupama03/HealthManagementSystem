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

background_image=tk.PhotoImage(file="hp pic 2.png")
background_label=tk.Label(root,image=background_image)
background_label.place(relwidth=1,relheight=1)

f1=tk.Frame(root, borderwidth=8,bg="#104E8B")
f1.pack(side='top',fill='x')

l=tk.Label(f1,text="APPENDIX",fg="#F0FFF0",bg="#104E8B",font=("Comic Sans MS","30" ," bold"))
l.pack()

intro= '''  During the 21st century the pooled incidence of
                appendicitis or appendectomy (in per 100,000 person-years) was 100 (95% CI: 91, 110) in
                Northern America, and the estimated number of cases in 2015 was 378,614.
                The pooled incidence ranged from 105 in Eastern Europe to 151 in Western Europe
                                    '''
introduction =tk.Label(root,text=intro,bg='#F0FFF0',fg='#104E8B',font=('calibri',22),justify='center')
introduction.place(x=150,y=200)
