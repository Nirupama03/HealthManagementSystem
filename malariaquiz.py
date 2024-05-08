import tkinter as tk
from tkinter import messagebox

q=["DO YOU HAVE HIGH FEVER","DO YOU HAVE HEADACHE","DO YOU HAVE PROFUSE SWEATING",
               "DO YOU HAVE NAUSEA","DO YOU HAVE ABDOMINAL PAIN"]


options =[["yes","no"],["yes","no"],["yes","no"],["yes","no"],["yes","no"]]

a=[2,2,2,2,2]

class Quiz:

    
    def __init__ (self,master=None):
        if master==None:
            master={}
        else:
            self.opt_selected=tk.IntVar()
            self.qn=0
            self.correct=0
            self.ques=self.create_q(master,self.qn)
            self.opts=self.create_options(master,2)
            self.display_q(self.qn)
            self.button=tk.Button(master,text="NEXT",command=self.next_btn,width=20,font=40,bg="#8DB6CD",pady=20)
            self.button.pack(side="bottom",padx=100,pady=100)
    def create_q(self,master,qn):
        w=tk.Label(master,text=q[qn],font=("Comic Sans MS","30" ," bold"),bg="#EE7621")
        w.pack(side="top",padx=20,pady=20)
        return w
    def create_options(self,master,n):
        b_val=0
        b=[]
        while b_val < n:
            btn=tk.Radiobutton(master,text="foo",variable=self.opt_selected,value=b_val+1,font=("arial",25,"bold"),bg="#7FFF00")
            b.append(btn)
            btn.pack(side="top",padx=30,pady=30)
            b_val=b_val+1
        return b
    def display_q(self,qn):
        b_val=0
        self.opt_selected.set(0)
        self.ques['text']=q[qn]
        for op in options[qn]:
            self.opts[b_val]['text']=op
            b_val=b_val+1

    def check_q(self,qn):
        if self.opt_selected.get()==a[qn]:
            return True
        return False
    
    def print_results(self):
           hui=tk.messagebox.showinfo("RESULT","YOU DONT HAVE ANY PROBLEM..YOU ARE ABSOLUTELY FINE")
           if hui=="ok":
                response=messagebox.askyesno("Feedback","WE VALUE YOUR FEEDBACK !!")
                if response==1:
                         root.destroy()
                         from Healthapp import feedbackform
                else:
                         thankyou=messagebox.showinfo("THANKYOU!!!","THANKYOU VERY MUCH FOR YOUR VALUABLE TIME!!!!!")
    def next_btn(self):
        if self.check_q(self.qn):
            self.correct=self.correct+1
            self.qn=self.qn+1
        else:
            self.qn=self.qn+1
        if self.qn == len(q):
            if self.correct>=3:
                self.print_results()
            elif self.correct==2:
                hui=tk.messagebox.showinfo("RESULT","YOU DON'T HAVE  ALL THE SYMPTOMS OF MALARIA. BUT IT WOULD BE GOOD IF YOU  CONSULT A DOCTOR")
                if hui=="ok":
                     response=messagebox.askyesno("Feedback","WE VALUE YOUR FEEDBACK !!")
                     if response==1:
                         root.destroy()
                         from Healthapp import feedbackform
                     else:
                         thankyou=messagebox.showinfo("THANKYOU!!!","THANKYOU VERY MUCH FOR YOUR VALUABLE TIME!!!!!") 
                
            else:
                hui=tk.messagebox.showinfo("RESULT","YOU HAVE SYMPTOMS OF MALARIA. PLEASE CONSULT A DOCTOR")
                if hui=="ok":
                     response=messagebox.askyesno("Feedback","WE VALUE YOUR FEEDBACK !!")
                     if response==1:
                         root.destroy()
                         from Healthapp import feedbackform
                     else:
                         thankyou=messagebox.showinfo("THANKYOU!!!","THANKYOU VERY MUCH FOR YOUR VALUABLE TIME!!!!!")
        else:
            self.display_q(self.qn)
 

root=tk.Tk()
root.geometry("1920x1080")
photo=tk.PhotoImage(file='doc icon.png')
icon=root.iconphoto(False,photo)

background_image=tk.PhotoImage(file="final pic 2.png")
background_label=tk.Label(root,image=background_image)
background_label.place(relwidth=1,relheight=1)

yay=messagebox.showinfo("CAUSE FOR MALARIA",'''   Caused by the Plasmodium parasite
 Malaria is not spread from person to person like a cold or the flu, and it cannot be sexually transmitted.
It Spreads By animal or insect bites or stings.By blood products (unclean needles or unscreened blood)''')


app=Quiz(root)
root.mainloop()




