from tkinter import *
import pymysql
con=pymysql.Connect(user="root", password="123456", host="localhost", port=3306)
cur=con.cursor()
cur.execute("create database if not exists bank_details")
con=pymysql.connect(user="host", password="123456", host="localhost", database="bank_details")
cur=con.cursor()
cur.execute("create table if not exists app(Accountnumber VarChar(30), Name VarChar(20), Dateofbirth VarChar(20), Gender VarChar(10), Age Int(2), Community VarChar(10), Accounttype VarChar(30), Aadhaarnumber VarChar(30), Pannumber VarChar(30), Fathername Varchar(30), Mobileno Int(10), Address VarChar(30), Date VarChar(20), Balance Int(10))")
cur.execute("commit")

a=Tk()
f=("times new roman", 14)
b="yellow"
f1="BLACK"
a.state("zoomed")
Accountnumber= StringVar()
Name= StringVar()
Dateofbirth= StringVar()
Gender= StringVar()
Age= IntVar()
Community= StringVar()
Accounttype= StringVar()
Aadhaarnumber= StringVar()
Pannumber= StringVar()
Fathername= StringVar()
Mobileno= IntVar()
Address= StringVar()
Date= StringVar()
Balance= IntVar()

#LABEL
Label(a,text="BANK DETAILS", font=("times new roman",40)).pack()
Label(a,text="ACCOUNT NUMBER", fg=f1, font=f).place(x=50,y=70)
Label(a,text="NAME", fg=f1, font=f).place(x=50,y=110)
Label(a,text="DATE OF BIRTH", fg=f1, font=f).place(x=50,y=150)
Label(a,text="GENDER", fg=f1, font=f).place(x=50,y=190)
Label(a,text="AGE", fg=f1, font=f).place(x=50,y=230)
Label(a,text="COMMUNITY", fg=f1, font=f).place(x=50,y=270)
Label(a,text="ACCOUNT TYPE", fg=f1, font=f).place(x=50,y=310)
Label(a,text="AADHAAR NUMBER", fg=f1, font=f).place(x=50,y=350)
Label(a,text="PAN NUMBER", fg=f1, font=f).place(x=50,y=390)
Label(a,text="FATHER NAME", fg=f1, font=f).place(x=50,y=430)
Label(a,text="MOBILE NUMBER", fg=f1, font=f).place(x=50,y=470)
Label(a,text="ADDRESS", fg=f1, font=f).place(x=50,y=510)
Label(a,text="DATE", fg=f1, font=f).place(x=50,y=550)
Label(a,text="BALANCE", fg=f1, font=f).place(x=50,y=590)

#ENTRY
Entry(a,textvariable= Accountnumber, font=f).place(x=260,y=70)
Entry(a,textvariable= Name, font=f).place(x=260,y=110)
Entry(a,textvariable= Dateofbirth, font=f).place(x=260,y=150)
Entry(a,textvariable= Age, font=f).place(x=260,y=230)
Entry(a,textvariable= Aadhaarnumber, font=f).place(x=260,y=350)
Entry(a,textvariable= Pannumber, font=f).place(x=260,y=390)
Entry(a,textvariable= Fathername, font=f).place(x=260,y=430)
Entry(a,textvariable= Mobileno, font=f).place(x=260,y=470)
Entry(a,textvariable= Address, font=f).place(x=260,y=510)
Entry(a,textvariable= Date, font=f).place(x=260,y=550)
Entry(a,textvariable= Balance, font=f).place(x=260,y=590)

#RADIO BUTTON
Radiobutton(a,text="MALE", font=f, value="Male", variable=Gender).place(x=260,y=190)
Radiobutton(a,text="FEMALE", font=f, value="Female", variable=Gender).place(x=380,y=190)
Radiobutton(a,text="OTHERS", font=f, value="Others", variable=Gender).place(x=500,y=190)
Radiobutton(a,text="CURRENT", font=f, value="Current", variable=Accounttype).place(x=260,y=310)
Radiobutton(a,text="SAVINGS", font=f, value="Savings", variable=Accounttype).place(x=380,y=310)

#SPIN BOX
Spinbox(a,textvariable=Community,values=("OC","BC","MBC","SC","ST"), font=f, bd=4).place(x=260,y=270)

def Save():
    cur.execute("insert inta app values('%s','%s','%s','%s',%d,'%s','%s','%s','%s','%s',%d,'%s','%s',%d)"%(Accountnumber.get(),Name.get(),Dateofbirth.get(),Gender.get(),Age.get(),Community.get(),Accounttype.get(),Aadhaarnumber.get(),Pannumber.get(),Fathername.get(),Mobileno.get(),Address.get(),Date.get(),Balance.get()))
    cur.execute("commit")

def Exit():
    a.destroy()

Button(a,text="SAVE",font=f,command=Save).place(x=260,y=650)
Button(a,text="EXIT",font=f,command=Exit).place(x=360,y=650)

a.mainloop()