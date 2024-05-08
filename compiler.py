import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import random as r 
import time as t
from datetime import datetime
now = datetime.now()
import csv

root=tk.Tk()
root.geometry("700x500")
title=root.title("SOINS DE SANTE")
photo=tk.PhotoImage(file='doc icon.png')
icon=root.iconphoto(False,photo)

background_image=tk.PhotoImage(file="newpics.png")
background_label=tk.Label(root,image=background_image)
background_label.place(relwidth=1,relheight=1)

f1=tk.Frame(root, borderwidth=8,bg="#ADADAD")
f1.pack(side='top',fill='x')

l=tk.Label(f1,text="WELCOME TO SOINS DE SANTE : YOUR HEALTH OUR PRIORITY !",fg="#141414",bg="#ADADAD",font=("Californian FB","27" ," bold"))
l.pack()

f2=tk.Frame(root,padx=10,pady=10,bg='#ADADAD')
f2.pack(padx=200,pady=190)

response=messagebox.askyesno("Question","Do you have a registration number??")


def start_quiz():

                intro= ''' :: How to take the QnA ::
                    ..................................................................................................................
                    1.You will be asked to choose the option for the QnA
                    2.There will be 5 to 6 questions related to the ailment
                    3.Ans the question in yes/no
                    4.The result will be published as soon as the QnA gets over
                    5.Please choose the ailment u have to check.
                    ..................................................................................................................
                                                                                                            '''


                #===========================================TITLE===================================================

                title='''  SOINS DE SANTE : YOUR HEALTH OUR PRIORITY!!!

                '''
                f4=tk.Frame(root, borderwidth=2,bg="#ADADAD")
                f4.pack(side='top',fill='x')
                appname=tk.Label(f4,text=title,font=('impact',23,'italic'),bg='#ADADAD',fg='white')
                appname.pack()

                #=====================================================================================================


                #=========================CURRENT Q================================================================
                queLabel=tk.Label(root,text='',justify='left',font=25)
                queLabel.pack(side='top',fill='both')


                #===================================INTRODUCTION TO THE QUIZ========================================

                introduction =tk.Label(root,text=intro,bg='#ADADAD',fg='white',font=('calibri',20),justify='center')
                introduction.place(x=170,y=200)

                #=====================================DROP DOWN BOX===================================================


                l=["STATISTICS RELATED TO  THE DISEASE","INSTANT BMI CHECKER","DENGUE","CHOLERA","TUBERCULOSIS","MIGRANE","CHICKENPOX","MALARIA","JAUNDICE","PNEUMONIA","ARTHRITIS","CORONA","DEPRESSION",
                   "MENINGITIS","OBEISITY","ANXEITY","BULIMIA","APPENDIX","POST TRAUMATIC STRESS DISORDER"]
                
                def  selected(event):
                    if clicked.get()=="DENGUE":
                                    appname.destroy()
                                    queLabel.destroy()
                                    introduction.destroy()
                                    drop.destroy()
                                    root.destroy()
                                    from Healthapp import denguequiz
                                    denguequiz.Quiz()
                            
                        
                    elif clicked.get()=="CHOLERA":                        
                        appname.destroy()
                        queLabel.destroy()
                        introduction.destroy()
                        drop.destroy()
                        root.destroy()
                        from Healthapp import choleraquiz
                        choleraquiz.Quiz()
                        

                    elif clicked.get()=="TUBERCULOSIS":
                        appname.destroy()
                        queLabel.destroy()
                        introduction.destroy()
                        drop.destroy()
                        root.destroy()
                        from Healthapp import tuberculosisquiz
                        tuberculosisquiz.Quiz()
                        
                    elif clicked.get()=="MIGRANE":
                        appname.destroy()
                        queLabel.destroy()
                        introduction.destroy()
                        drop.destroy()
                        root.destroy()
                        from Healthapp import migranequiz
                        migranequiz.Quiz()
                        
                    elif clicked.get()=="CHICKENPOX":
                        appname.destroy()
                        queLabel.destroy()
                        introduction.destroy()
                        drop.destroy()
                        root.destroy()
                        from Healthapp import migranequiz
                        migranequiz.Quiz()
                     
                    elif clicked.get()=="MALARIA":
                        appname.destroy()
                        queLabel.destroy()
                        introduction.destroy()
                        drop.destroy()
                        root.destroy()
                        from Healthapp import malariaquiz
                        malariaquiz.Quiz()
                        
                    elif clicked.get()=="JAUNDICE":
                        appname.destroy()
                        queLabel.destroy()
                        introduction.destroy()
                        drop.destroy()
                        root.destroy()
                        from Healthapp import jaundicequiz
                        jaundicequiz.Quiz()
                        
                    elif clicked.get()=="PNEUMONIA":
                        appname.destroy()
                        queLabel.destroy()
                        introduction.destroy()
                        drop.destroy()
                        root.destroy()
                        from Healthapp import pneumoniaquiz
                        pneumoniaquiz.Quiz()
                        
                    elif clicked.get()=="ARTHRITIS":
                        appname.destroy()
                        queLabel.destroy()
                        introduction.destroy()
                        drop.destroy()
                        root.destroy()
                        from Healthapp import arthritisquiz
                        arthritisquiz.Quiz()
                        
                    elif clicked.get()=="CORONA":
                        appname.destroy()
                        queLabel.destroy()
                        introduction.destroy()
                        drop.destroy()
                        root.destroy()
                        from Healthapp import coronaquiz
                        coronaquiz.Quiz()
                        
                    elif clicked.get()=="DEPRESSION":
                        appname.destroy()
                        queLabel.destroy()
                        introduction.destroy()
                        drop.destroy()
                        root.destroy()
                        from Healthapp import depressionquiz
                        depressionquiz.Quiz()
                        
                    elif clicked.get()=="MENINGITIS":
                        appname.destroy()
                        queLabel.destroy()
                        introduction.destroy()
                        drop.destroy()
                        root.destroy()
                        from Healthapp import maningitisquiz
                        maningitisquiz.Quiz()
                       
                    elif clicked.get()=="OBEISITY":
                        appname.destroy()
                        queLabel.destroy()
                        introduction.destroy()
                        drop.destroy()
                        root.destroy()
                        from Healthapp import obesityquiz
                        obesityquiz.Quiz()
                        
                    elif clicked.get()=="ANXEITY":
                        appname.destroy()
                        queLabel.destroy()
                        introduction.destroy()
                        drop.destroy()
                        root.destroy()
                        from Healthapp import anxeityquiz
                        anxeityquiz.Quiz()
                       
                    elif clicked.get()=="BULIMIA":
                        appname.destroy()
                        queLabel.destroy()
                        introduction.destroy()
                        drop.destroy()
                        root.destroy()
                        from Healthapp import bulimiaquiz
                        bulimiaquiz.Quiz()
                        
                    elif clicked.get()=="APPENDIX":
                        appname.destroy()
                        queLabel.destroy()
                        introduction.destroy()
                        drop.destroy()
                        root.destroy()
                        from Healthapp import appendixquiz
                        appendixquiz.Quiz()
                        
                    elif clicked.get()=="POST TRAUMATIC STRESS DISORDER":
                        appname.destroy()
                        queLabel.destroy()
                        introduction.destroy()
                        drop.destroy()
                        root.destroy()
                        from Healthapp import ptsdquiz
                        ptsdquiz.Quiz()
                    elif clicked.get()=="INSTANT BMI CHECKER":
                        appname.destroy()
                        queLabel.destroy()
                        introduction.destroy()
                        drop.destroy()
                        root.destroy()
                        from Healthapp import BMI                        
                        
                    elif clicked.get()=="STATISTICS RELATED TO  THE DISEASE":
                        appname.destroy()
                        queLabel.destroy()
                        introduction.destroy()
                        drop.destroy()
                        root.destroy()
                        from Healthapp import STATISTICS


                clicked=tk.StringVar()
                clicked.set(l[0])

            
                drop=tk.OptionMenu(root,clicked,*l,command=selected)
                drop.pack(side="bottom",padx=30,pady=30)

                heloLabel=tk.Label(root,text="Select the ailment ",font=("Comic Sans MS","30" ," bold"),bg="#ADADAD",fg="white")
                heloLabel.pack(side="bottom",pady=40,padx=20)
                                
                                    


if response ==1:
    
        def submit():
                with open("regtfile.csv",'a+',newline='') as f:
                    w=csv.writer(f)
                    a=cid.get()
                    b=n.get()
                    c=age.get()
                    d=email.get()
                    e=gender.get()
                    k = now.strftime("%d/%m/%Y, %H:%M:%S")

                    w.writerow(["Crnt Date&Time","Reg ID","Name","Age","Email ID","Gender"])
                    w.writerow([k,a,b,c,d,e])
                    r=csv.reader(f,delimiter=' ')
        
                
                f.close()
                #CLEAR THE TEXTS
                cid.delete(0,50)
                n.delete(0,50)
                age.delete(0,50)
                email.delete(0,50)
                gender.delete(0,50)

                f1.destroy()
                l.destroy()
                f2.destroy()
                mybutton.destroy()

                start_quiz()



                
               

        cid= tk.Entry(f2,width=75,bd=6,bg='#E3E3E3',font=('Calisto MT',15))
        n=tk.Entry(f2,width=75,bd=6,bg='#E3E3E3',font=('Calisto MT',15))
        age=tk.Entry(f2,width=75,bd=6,bg='#E3E3E3',font=('Calisto MT',15))
        email=tk.Entry(f2,width=75,bd=6,bg="#E3E3E3",font=('Calisto MT',15))
        gender=tk.Entry(f2,width=75,bd=6,bg="#E3E3E3",font=('Calisto MT',15))
        cid.insert(0," CID(Enter your 4-digit ID):")
        n.insert(0,"NAME:")
        age.insert(0,"AGE:")
        email.insert(0,"EMAIL:")
        gender.insert(0,"GENDER:")
        cid.pack(padx=2,pady=2)
        n.pack(padx=2,pady=2)
        age.pack(padx=2,pady=2)
        email.pack(padx=2,pady=2)
        gender.pack(padx=2,pady=2)

        mybutton=tk.Button(f2,text="SUBMIT",command=submit  ,width=15,font=20,bg="#8DB6CD",pady=10)
        mybutton.pack()
else:
        reply=messagebox.askyesno("Reply","would u like to get a registration number ??")
        if reply==1:
                w=r.randint(1000,9999)
                messagebox.showinfo("Your Reg no is:",w)

        root.mainloop()

