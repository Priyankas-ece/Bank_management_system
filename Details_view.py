from tkinter import *
a=Tk()
f=("times nwe roman",14)
b="yellow"
f1="black"
a.state("zoomed")
no=StringVar()
Label(a,text="DETAILS VIEW",fg=f1,font=f).pack()
import pymysql
con=pymysql.Connect(user="root",password="",host="localhost",database="bank_details")
cur=con.cursor()

def Check():
    cur.execute("select * from app")
    rec=cur.fetchal()
    flag=0
    for i in rec:
        if i[0]==no.get():
            Label(a,text="NAME:"+i[1],fg=f1,font=f).place(x=50,y=110)
            Label(a,text="DATE OF BIRTH:"+i[2],fg=f1,font=f).place(x=50,y=150)
            Label(a,text="GENDER:"+i[3],fg=f1,font=f).place(x=50,y=190)
            Label(a,text="AGE:"+str(i[4]),fg=f1,font=f).place(x=50,y=230)
            Label(a,text="COMMUNITY:"+i[5],fg=f1,font=f).place(x=50,y=270)
            Label(a,text="ACCOUNT TYPE:"+i[6],fg=f1,font=f).place(x=50,y=310)
            Label(a,text="AADHAAR NUMBER:"+i[7],fg=f1,font=f).place(x=50,y=350)
            Label(a,text="PAN NUMBER:"+i[8],fg=f1,font=f).place(x=50,y=390)
            Label(a,text="FATHER NAME:"+i[9],fg=f1,font=f).place(x=50,y=430)
            Label(a,text="MOBILE NUMBER:"+str(i[10]),fg=f1,font=f).place(x=50,y=470)
            Label(a,text="ADDRESS:"+i[11],fg=f1,font=f).place(x=50,y=510)
            Label(a,text="DATE:"+i[12],fg=f1,font=f).place(x=50,y=550)
            Label(a,text="BALANCE:"+str(i[13]),fg=f1,font=f).place(x=50,y=590)

Label(a,text="ACCOUNT NUMBER",fg=f1,font=f).place(x=50,y=70)
Entry(a,textvariable=no,font=f).place(x=260,y=70)
Button(a,text="CHECK",font=f,command=Check).place(x=350,y=110)            

def Exit():
    a.destroy()

Button(a,text="EXIT",font=f,command=Exit).place(x=50,y=630)
a.mainloop()