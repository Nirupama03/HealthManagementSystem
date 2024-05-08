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

background_image=tk.PhotoImage(file="hp pic 4.png")
background_label=tk.Label(root,image=background_image)
background_label.place(relwidth=1,relheight=1)

f1=tk.Frame(root, borderwidth=8,bg="#104E8B")
f1.pack(side='top',fill='x')

l=tk.Label(f1,text="BULIMIA",fg="#F0FFF0",bg="#104E8B",font=("Comic Sans MS","30" ," bold"))
l.pack()

intro= '''  Eating disorders affect at least 9% of the population worldwide.
                19% of the U.S. population, or 28.8 million Americans, will have an
                eating disorder in their lifetime.2
                Less than 6% of people with eating disorders are medically diagnosed
                as “underweight.”
                28-74% of risk for eating disorders is through genetic heritability.
                Eating disorders are among the deadliest mental illnesses,
                second only to opioid overdose.
                10,200 deaths each year are the direct result of an
                eating disorder—that’s one death every 52 minutes.2
                About 26% of people with eating disorders attempt suicide.
                The economic cost of eating disorders is $64.7 billion every year.
                                    '''
introduction =tk.Label(root,text=intro,bg='#F0FFF0',fg='#104E8B',font=('calibri',22),justify='center')
introduction.place(x=150,y=100)
