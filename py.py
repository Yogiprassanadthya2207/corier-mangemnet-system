from tkinter import *
from PIL import ImageTk, Image
import tkinter .messagebox as MessageBox
import random
Names=[]
Reg_number=[]
Gender=[]
Mobileno=[]
Emailid=[]
username=[]
def call():
    t=Toplevel()
    t.geometry('1920x1080')
    t.configure(bg='#00008B')
    l=Label(t, text="Choose the Register",font=('Arial','18', "italic"),bg='#000000',height=1,width=40, fg='white')
    l.place(x=350, y=150)
    Button(t, text="Sign-Up",command=signup,height=1,width=10,bg='#00ffff',font=('Arial','12', "italic")).place(x=380,y=245)
    Button(t, text="Login",command=login,height=1,width=10,bg='#00ffff',font=('Arial','12', "italic")).place(x=570,y=245)
    Button(t, text="Track order", command= track, height=1, width=10, bg='#00ffff', font=('Arial', '12', "italic")).place(x=740, y=245)
def track():
    m=Toplevel()
    l = Label(m, text="Track order form", font=('Arial', '18', "italic"), bg='#000000', height=1, width=35, fg='white')
    l.place(x=360, y=130)
    m.geometry('1920x1080')
    m.configure(bg="#FEE23E")

    global tentry1
    global tentry2
    global tentry3
    global tentry4

    Label(m, text="User Name :", font=('Arial', '13', "italic"), bg="#FEE23E").place(x=500, y=250)
    Label(m, text="Order number :", font=('Arial', '13', "italic"), bg="#FEE23E").place(x=500, y=300)
    Label(m, text="Verfication id :", font=('Arial', '13', "italic"), bg="#FEE23E").place(x=500, y=350)
    Label(m, text="Package no :", font=('Arial', '13', "italic"), bg="#FEE23E").place(x=500, y=400)
    Button(m,text="Check status",bg='#800080',command=status,font=('Arial', '13', "italic")).place(x=550,y=500)

    tentry1=Entry(m,bd=5)
    tentry1.place(x=620,y=250)

    tentry2=Entry(m,bd=5)
    tentry2.place(x=620,y=300)

    tentry3=Entry(m,bd=5)
    tentry3.place(x=620,y=350)

    tentry4=Entry(m,bd=5)
    tentry4.place(x=620,y=400)

def status():
    MessageBox.showinfo("","hello coustomer  "   + 'your order will delivered on friday')
def signup():
    i=Toplevel()
    l = Label(i, text="Signup Form",font=('Arial','18', "italic"),bg='#000000',height=1,width=35, fg='white')
    l.place(x=360, y=130)
    i.geometry('1920x1080')
    i.configure(bg="#FEE23E")
    global rntry1
    global rntry2
    global rntry3
    global rntry4
    global rntry5
    global rntry6

    Label(i, text="Name :",font=('Arial','13', "italic"),bg="#FEE23E").place(x=500,y=250)
    Label(i, text="Reg_number :",font=('Arial','13', "italic"),bg="#FEE23E").place(x=500,y=300)
    Label(i, text="Gender :", font=('Arial', '13', "italic"), bg="#FEE23E").place(x=500, y=350)
    Label(i, text="Mobile no :", font=('Arial', '13', "italic"), bg="#FEE23E").place(x=500, y=400)
    Label(i, text="Email id :", font=('Arial', '13', "italic"), bg="#FEE23E").place(x=500, y=450)
    Button(i,text="Register",bg='#800080',command=register,font=('Arial', '13', "italic")).place(x=590,y=500)

    rntry1=Entry(i,bd=5)
    rntry1.place(x=620,y=250)

    rntry2=Entry(i, bd=5)
    rntry2.place(x=620, y=300)

    rntry3=Radiobutton(i,text='Male',bg='#FEE23E',value=0,font=('Arial', '13', "italic"))
    rntry3.place(x=620,y=350)

    rntry4=Radiobutton(i,text='Female',bg='#FEE23E',value=1,font=('Arial', '13', "italic"))
    rntry4.place(x=700, y=350)

    rntry5=Entry(i, bd=5)
    rntry5.place(x=620, y=400)

    rntry6 = Entry(i, bd=5)
    rntry6.place(x=620, y=450)

def register():
    name=rntry1.get()
    reg_no=rntry2.get()
    mobileno=rntry5.get()
    emailid=rntry6.get()
    Names.append(name)
    Reg_number.append(reg_no)
    Mobileno.append(mobileno)
    Emailid.append(emailid)
    uname=str(random.randint(11111,99999))
    username.append(uname)
    MessageBox.showinfo('','Your Username :'+uname)

def login():
    s=Toplevel()
    l = Label(s, text="Login Form",font=('Arial','18', "italic"),bg='#000000',height=1,width=35, fg='white')
    l.place(x=360, y=130)
    s.geometry('1920x1080')
    s.configure(bg="#86B404")
    global entry1
    global entry2

    Label(s, text="Username :",font=('Arial','13', "italic"),bg="#86B404").place(x=500,y=250)
    Label(s, text="Password :",font=('Arial','13', "italic"),bg="#86B404").place(x=500,y=300)

    entry1=Entry(s,bd=5)
    entry1.place(x=620,y=250)

    entry2=Entry(s, bd=5)
    entry2.place(x=620, y=300)

    Button(s,text="Submit",height=1,width=10,bg='#FFFFFF',command=submit).place(x=587,y=400)
def submit():
    uname1 = entry1.get()
    Password1 = entry2.get()
    if uname1 in username:
        for i in username:
            i=username.index(uname1)
        if Password1==Reg_number[i]:
            MessageBox.showinfo(uname1, "logged successfully New user")
        else:
            MessageBox.showinfo(uname1, "Wrong Credential")
    else:
            MessageBox.showinfo("","Invalid inputs")
root = Tk()
root.geometry('1920x1080')
root.configure(bg='#ff4f5a')
root.title("Project 14")
title = Label(root,text="Lpu's Courier Management System",font=('Arial','18','italic'),bg='#ff4f5a',fg='white')
title.place(x=450, y=190)
Getstarted=Button(root,text="Get started",width=10, height=1,bg='#87CEEB',fg='black',font=('Arial','18','italic'),command=call)
Getstarted.place(x=550,y=250)
root.mainloop()