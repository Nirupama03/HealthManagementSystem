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

background_image=tk.PhotoImage(file="hp pic 8.png")
background_label=tk.Label(root,image=background_image)
background_label.place(relwidth=1,relheight=1)

f1=tk.Frame(root, borderwidth=8,bg="#9932CC")
f1.pack(side='top',fill='x')

l=tk.Label(f1,text="OBESITY",fg="#9932CC",bg="#00EEEE",font=("Comic Sans MS","30" ," bold"))
l.pack()

intro= '''  In 2016, more than 1.9 billion adults aged 18 years and older were overweight. Of these over 650 million adults were obese.
                In 2016, 39% of adults aged 18 years and over (39% of men and 40% of women) were overweight.
                Overall, about 13% of the world’s adult population (11% of men and 15% of women) were obese in 2016.
                The worldwide prevalence of obesity nearly tripled between 1975 and 2016.
                In 2019, an estimated 38.2 million children under the age of 5 years were overweight or obese.
                Once considered a high-income country problem, overweight and obesity are now
                on the rise in low- and middle-income countries, particularly in urban settings.
                In Africa, the number of overweight children
                under 5 has increased by nearly 24% percent since 2000.
                Almost half of the children under 5 who were overweight or obese in 2019 lived in Asia.
                Over 340 million children and adolescents aged 5-19 were overweight or obese in 2016.
                The prevalence of overweight and obesity among children and adolescents aged 5-19 has
                risen dramatically from just 4% in 1975 to just over 18% in 2016.
                The rise has occurred similarly among both boys and girls: in 2016 18% of girls and 19% of boys were overweight.
                While just under 1% of children and adolescents aged 5-19 were obese in 1975,
                more 124 million children and adolescents (6% of girls and 8% of boys) were obese in 2016.
                                    '''
introduction =tk.Label(root,text=intro,bg='#7CFC00',fg='white',font=('calibri',17),justify='center')
introduction.place(x=150,y=100)
