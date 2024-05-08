#BMI CHECKER
import tkinter as tk
from tkinter import messagebox
import random as r
HEIGHT=1920
WIDTH=1080
root=tk.Tk()
canvas=tk.Canvas(root,height=HEIGHT,width=WIDTH)
canvas.place()
title=root.title("SOINS DE SANTE")
photo=tk.PhotoImage(file='doc icon.png')
icon=root.iconphoto(False,photo)

background_image=tk.PhotoImage(file="docybg.png")
background_label=tk.Label(root,image=background_image)
background_label.place(relwidth=1,relheight=1)
f1=tk.Frame(root, borderwidth=8,bg="#104E8B")
f1.pack(side='top',fill='x')

l=tk.Label(f1,text="INSTANT BMI CHECKER",fg="#FFFAF0",bg="#104E8B",font=("Comic Sans MS","29" ," bold"))
l.pack()

frame=tk.Frame(root,padx=10,pady=10,bg='#104E8B')
frame.pack(padx=200,pady=200)

response=messagebox.askyesno("Query","Are you an Adult ??")
if response ==1:
         weight=tk.IntVar()
         height=tk.IntVar()
         def submit():
                         global weight,height
                         weight=weight.get()
                         height=height.get()/1000
                         BMI1=(weight/((height**2)))/100
                         result=messagebox.showinfo("RESULT",f"your BMI is : {BMI1}")
                         if BMI1<18.5:
                                result=messagebox.showinfo("RESULT",
                                                       ''' you are Underweight\n Here are some healthy ways to gain weight when you're underweight:\n
                                                               1)Eat more frequently
                                                               2)Exercise, especially strength training, can help you gain weight by building up your muscles''')
                                if result=="ok":
                                    response=messagebox.askyesno("Feedback","WE VALUE YOUR FEEDBACK !!")
                                    if response==1:
                                             root.destroy()
                                             from Healthapp import feedbackform
                                    else:
                                             thankyou=messagebox.showinfo("THANKYOU!!!","THANKYOU VERY MUCH FOR YOUR VALUABLE TIME!!!!!")
                         elif  18.5<BMI1<24.9:
                                 result=messagebox.showinfo("RESULT","you are of normal weight")
                                 if result=="ok":
                                     response=messagebox.askyesno("Feedback","WE VALUE YOUR FEEDBACK !!")
                                     if response==1:
                                             root.destroy()
                                             from Healthapp import feedbackform
                                     else:
                                             thankyou=messagebox.showinfo("THANKYOU!!!","THANKYOU VERY MUCH FOR YOUR VALUABLE TIME!!!!!")
                         elif 25<BMI1<29.9:
                                 result=messagebox.showinfo("RESULT",
                                                    ''' you are Overweight \n Here are some healthy ways to lose weight when you're overweight:\n
                                                            1)Diet
                                                            2)Regular exercise such as brisk walking, running, swimming, biking, dancing.''')
                                 if result=="ok":
                                     response=messagebox.askyesno("Feedback","WE VALUE YOUR FEEDBACK !!")
                                     if response==1:
                                             root.destroy()
                                             from Healthapp import feedbackform
                                     else:
                                             thankyou=messagebox.showinfo("THANKYOU!!!","THANKYOU VERY MUCH FOR YOUR VALUABLE TIME!!!!!")
                         else:
                                result=messagebox.showinfo("RESULT",
                                                       '''  you are Obese \n Here are some healthy ways to lose weight when you're obese
                                                            “Reduce calories by 500 calories per day to lose about a one pound a week, or cut 1,000 calories
                                                            a day to lose about twopounds a week.Consider adding physical activity after reaching
                                                            a minimum of 10 percent weight-loss goal.''')
                                if result=="ok":
                                    response=messagebox.askyesno("Feedback","WE VALUE YOUR FEEDBACK !!")
                                    if response==1:
                                             root.destroy()
                                             from Healthapp import feedbackform
                                    else:
                                             thankyou=messagebox.showinfo("THANKYOU!!!","THANKYOU VERY MUCH FOR YOUR VALUABLE TIME!!!!!")
        
         weight_entry= tk.Entry(frame,textvariable=weight,width=75,bd=6,bg='#FFFAF0',font=70)
         height_entry=tk.Entry(frame,textvariable=height,width=75,bd=6,bg='#FFFAF0',font=70)
         weight_entry.insert(0," ENTER YOUR WEIGHT:")
         height_entry.insert(0,"ENTER YOUR HEIGHT:")
         weight_entry.pack(padx=2,pady=2)
         height_entry.pack(padx=2,pady=2)

         mybutton=tk.Button(frame,text="SUBMIT",command=submit  ,width=10,font=40,bg="#8DB6CD",pady=20)
         mybutton.pack()
else:
     result=messagebox.showinfo("Info","NOTE: BMI CANNOT BE CALCULATED FOR TEENAGERS AND GROWING CHILDREN")
     root.destroy()
