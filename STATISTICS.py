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

f1=tk.Frame(root, borderwidth=8,bg="#9932CC")
f1.pack(side='top',fill='x')

l=tk.Label(f1,text="WELCOME TO SOINS DE SANTE : YOUR HEALTH OUR PRIORITY!",fg="#9932CC",bg="#00EEEE",font=("Comic Sans MS","29" ," bold"))
l.pack()

l=["DENGUE","CHOLERA","TUBERCULOSIS","MIGRANE","CHICKENPOX","MALARIA","JAUNDICE","PNEUMONIA","ARTHRITIS","CORONA","DEPRESSION",
                   "MENINGITIS","OBEISITY","ANXEITY","BULIMIA","APPENDIX","POST TRAUMATIC STRESS DISORDER"]

def  selected(event):
                    if clicked.get()=="DENGUE":
                        root.destroy()
                        from Healthapp import picdengue            
                    elif clicked.get()=="CHOLERA":                        
                        root.destroy()
                        from Healthapp import piccholera                           
                    elif clicked.get()=="TUBERCULOSIS":
                        root.destroy()
                        from Healthapp import pictb                          
                    elif clicked.get()=="MIGRANE":
                        root.destroy()
                        from Healthapp import picmigrane                           
                    elif clicked.get()=="CHICKENPOX":
                        root.destroy()
                        from Healthapp import piccp                        
                    elif clicked.get()=="MALARIA":
                        root.destroy()
                        from Healthapp import picmalaria                          
                    elif clicked.get()=="JAUNDICE":
                        root.destroy()
                        from Healthapp import picjaundice                           
                    elif clicked.get()=="PNEUMONIA":
                        root.destroy()
                        from Healthapp import picpneumonia                          
                    elif clicked.get()=="ARTHRITIS":
                        root.destroy()
                        from Healthapp import picarthritis                   
                    elif clicked.get()=="CORONA":
                        root.destroy()
                        from Healthapp import piccorona                           
                    elif clicked.get()=="DEPRESSION":
                        root.destroy()
                        from Healthapp import picdepression 
                    elif clicked.get()=="MENINGITIS":
                        root.destroy()
                        from Healthapp import picmeningitis                         
                    elif clicked.get()=="OBEISITY":
                        root.destroy()
                        from Healthapp import picobesity                           
                    elif clicked.get()=="ANXEITY":
                        root.destroy()
                        from Healthapp import picanxiety                          
                    elif clicked.get()=="BULIMIA":
                        root.destroy()
                        from Healthapp import picbulimia                           
                    elif clicked.get()=="APPENDIX":
                        root.destroy()
                        from Healthapp import picappendix   
                    elif clicked.get()=="POST TRAUMATIC STRESS DISORDER":
                        root.destroy()
                        from Healthapp import picptsd
                    else:
                        MYlabel=tk.Label(root,text="Ran out of options!!").pack()


clicked=tk.StringVar()
clicked.set(l[0])

            
drop=tk.OptionMenu(root,clicked,*l,command=selected)
drop.pack(side="top",padx=30,pady=30)

heloLabel=tk.Label(root,text="Select the ailment to be viewed !!",font=("Comic Sans MS","30" ," bold"),bg="#DC143C",fg="#7FFF00")
heloLabel.pack(side="top",pady=40,padx=20)
